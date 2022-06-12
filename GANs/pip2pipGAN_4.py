import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils import data
import torchvision
from torchvision import transforms
 
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from PIL import Image
 
imgs_path = glob.glob('dataset/base/*.jpg')
annos_path = glob.glob('dataset/base/*.png')
 
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Resize((256, 256)),
                                transforms.Normalize(0.5,0.5)])
 
class CMP_dataset(data.Dataset):
    def __init__(self, imgs_path, annos_path):
        self.imgs_path = imgs_path
        self.annos_path = annos_path
    def __getitem__(self, index):
        img_path = self.imgs_path[index]
        anno_path = self.annos_path[index]
        pil_img = Image.open(img_path)
        pil_img = transform(pil_img)
        anno_img = Image.open(anno_path)
        anno_img = anno_img.convert('RGB')
        pil_anno = transform(anno_img)
        return pil_anno, pil_img
    def __len__(self):
        return len(imgs_path)
 
dataset = CMP_dataset(imgs_path, annos_path)
dataloader = data.DataLoader(dataset, batch_size=32, shuffle=True)
 
 
# 创建模型
# 定义下采样模块
class Downsample(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Downsample, self).__init__()
        self.conv_relu = nn.Sequential(
                            nn.Conv2d(in_channels, out_channels,
                                      kernel_size=3,
                                      stride=2,
                                      padding=1),
                            nn.LeakyReLU(inplace=True),
            )
        self.bn = nn.BatchNorm2d(out_channels)
 
    def forward(self, x, is_bn=True):
        x = self.conv_relu(x)
        if is_bn:
            x = self.bn(x)
        return x
 
# 定义上采用模块
class Upsample(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Upsample, self).__init__()
        self.upconv_relu = nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels,
                               kernel_size=3,
                               stride=2,
                               padding=1,
                               output_padding=1),
            nn.LeakyReLU(inplace=True)
        )
        self.bn = nn.BatchNorm2d(out_channels)
 
    def forward(self, x, is_drop=False):
        x = self.upconv_relu(x)
        x = self.bn(x)
        if is_drop:
            x = F.dropout2d(x)
        return x
 
# 定义生成器：六个下采样层，五个上采样层，一个输出层
# UNet结构
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.down1 = Downsample(3, 64)
        self.down2 = Downsample(64, 128)
        self.down3 = Downsample(128, 256)
        self.down4 = Downsample(256, 512)
        self.down5 = Downsample(512, 512)
        self.down6 = Downsample(512, 512)
 
        self.up1 = Upsample(512, 512)
        self.up2 = Upsample(1024, 512)
        self.up3 = Upsample(1024, 256)
        self.up4 = Upsample(512, 128)
        self.up5 = Upsample(256, 64)
 
        self.last = nn.ConvTranspose2d(128, 3,
                                       kernel_size=3,
                                       stride=2,
                                       padding=1,
                                       output_padding=1)
 
    def forward(self, x):
        x1 = self.down1(x, is_bn=False)  # torch.Size([8, 64, 128, 128])
        x2 = self.down2(x1)  # torch.Size([8, 128, 64, 64])
        x3 = self.down3(x2)  # torch.Size([8, 256, 32, 32])
        x4 = self.down4(x3)  # torch.Size([8, 512, 16, 16])
        x5 = self.down5(x4)  # torch.Size([8, 512, 8, 8])
        x6 = self.down6(x5)  # torch.Size([8, 512, 4, 4])
 
        x6 = self.up1(x6, is_drop=True)  # torch.Size([8, 512, 8, 8])
        x6 = torch.cat([x5, x6], dim=1)  # torch.Size([8, 1024, 8, 8])
 
        x6 = self.up2(x6, is_drop=True)  # torch.Size([8, 512, 16, 16])
        x6 = torch.cat([x4, x6], dim=1)  # torch.Size([8, 1024, 16, 16])
 
        x6 = self.up3(x6, is_drop=True)
        x6 = torch.cat([x3, x6], dim=1)
 
        x6 = self.up4(x6)
        x6 = torch.cat([x2, x6], dim=1)
 
        x6 = self.up5(x6)
        x6 = torch.cat([x1, x6], dim=1)
 
        x6 = torch.tanh(self.last(x6))
        return x6
 
# 判别器
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator,self).__init__()
        self.down1 = Downsample(6, 64)
        self.down2 = Downsample(64, 128)
        self.down3 = Downsample(128, 256)
        self.conv = nn.Conv2d(256, 512, 3, 1, 1)
        self.bn = nn.BatchNorm2d(512)
        self.last = nn.Conv2d(512, 1, 3, 1)
 
    def forward(self, anno, img):
        x = torch.cat([anno, img], dim=1)  # batch*6*H*W
        x = self.down1(x, is_bn=False)
        x = self.down2(x)
        x = F.dropout2d(self.down3(x))
        x = F.dropout2d(F.leaky_relu(self.conv(x)))
        x = F.dropout2d(self.bn(x))
        x = torch.sigmoid(self.last(x))
        return x
 
device = 'cuda' if torch.cuda.is_available() else 'cpu'
gen = Generator().to(device)
dis = Discriminator().to(device)
 
# 定义损失函数
# cgan损失函数
loss_fn = torch.nn.BCELoss()
 
d_optimizer = torch.optim.Adam(dis.parameters(), lr=2e-4, betas=(0.5, 0.999))
g_optimizer = torch.optim.Adam(gen.parameters(), lr=2e-4, betas=(0.5, 0.999))
 
# 绘图函数
def generate_images(model, test_input, true_target):
    prediction = model(test_input).permute(0, 2, 3, 1).detach().cpu().numpy()
    test_input = test_input.permute(0, 2, 3, 1).cpu().numpy()
    true_target = true_target.permute(0, 2, 3, 1).cpu().numpy()
    plt.figure(figsize=(5, 5))
    display_list = [test_input[0], true_target[0], prediction[0]]
    title = ['Input Image', 'Ground Truth', 'Predicted Image']
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.title(title[i])
        plt.imshow(display_list[i] * 0.5 + 0.5)
        plt.axis('off')
    plt.show()
 
test_imgs_path = glob.glob('dataset/extended/*.jpg')
test_annos_path = glob.glob('dataset/extended/*.png')
 
test_dataset = CMP_dataset(test_imgs_path, test_annos_path)
test_dataloader = data.DataLoader(test_dataset, batch_size=32)
 
LAMBDA = 10  # L1损失的权重
 
annos_batch, imgs_batch = next(iter(test_dataloader))
imgs_batch = imgs_batch.to(device)
annos_batch = annos_batch.to(device)
 
D_loss = []  # 记录训练过程中判别器loss变化
G_loss = []  # 记录训练过程中生成器loss变化
 
# 开始训练
for epoch in range(100):
    D_epoch_loss = 0
    G_epoch_loss = 0
    count = len(dataloader)
    for step, (annos, imgs) in enumerate(dataloader):
        imgs = imgs.to(device)
        annos = annos.to(device)
 
        d_optimizer.zero_grad()
        disc_real_output = dis(annos, imgs)  # 判别器输入真实图片
        d_real_loss = loss_fn(disc_real_output,
                              torch.ones_like(disc_real_output, device=device))
        d_real_loss.backward()
 
        # 生成器输入随机张量得到生成图片
        gen_output = gen(annos)
        disc_gen_output = dis(annos, gen_output.detach())
        d_fake_loss = loss_fn(disc_gen_output,
                              torch.zeros_like(disc_gen_output, device=device))
        d_fake_loss.backward()
 
        disc_loss = d_real_loss + d_fake_loss  # 判别器的总损失
        d_optimizer.step()
 
        g_optimizer.zero_grad()
 
        disc_gen_output = dis(annos, gen_output)  # 判别器输入生成图像
        gen_loss_crossentropy = loss_fn(disc_gen_output,
                                        torch.ones_like(disc_gen_output, device=device))
        gen_l1_loss = torch.mean(torch.abs(imgs - gen_output))  # L1损失
        gen_loss = gen_loss_crossentropy + (LAMBDA * gen_l1_loss)
        gen_loss.backward()
        g_optimizer.step()
 
        with torch.no_grad():
            D_epoch_loss += disc_loss.item()
            G_epoch_loss += gen_loss.item()
    #            generate_images(gen, imgs_batch, musks_batch)
    with torch.no_grad():
        D_epoch_loss /= count
        G_epoch_loss /= count
        D_loss.append(D_epoch_loss)
        G_loss.append(G_epoch_loss)
        # 训练完一个Epoch，打印提示并绘制生成的图片
        print("Epoch:", epoch)
        generate_images(gen, annos_batch, imgs_batch)