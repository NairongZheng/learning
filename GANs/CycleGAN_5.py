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
import itertools
 
 
# 加载训练数据
apples_path = glob.glob('data/trainA/*.jpg')
oranges_path = glob.glob('data/trainB/*.jpg')
 
 
 
transform = transforms.Compose([transforms.ToTensor(),  # 0-1归一化
                                transforms.Normalize(0.5, 0.5),  # -1，1
                                ])
 
class AppleOrangeDataset(data.Dataset):
    def __init__(self, img_path):
        self.img_path = img_path
 
    def __getitem__(self, index):
        img_path = self.img_path[index]
        pil_img = Image.open(img_path)
        pil_img = transform(pil_img)
        return pil_img
    def __len__(self):
        return len(self.img_path)
 
apple_dataset = AppleOrangeDataset(apples_path)
oranges_dataset = AppleOrangeDataset(oranges_path)
 
batch_size = 4
 
apples_dl = torch.utils.data.DataLoader(apple_dataset,
                               batch_size = batch_size,
                               shuffle = True)
 
oranges_dl = torch.utils.data.DataLoader(oranges_dataset,
                               batch_size = batch_size,
                               shuffle = True)
 
apples_batch = next(iter(apples_dl))    # 返回一个批次的训练数据
oranges_batch = next(iter(oranges_dl))    # 返回一个批次的训练数据
 
 
# 加载测试集
apples_test_path = glob.glob('data/testA/*.jpg')
oranges_test_path = glob.glob('data/testB/*.jpg')
 
apples_test_dataset = AppleOrangeDataset(apples_test_path)
oranges_test_dataset = AppleOrangeDataset(oranges_test_path)
 
apples_test_dl = torch.utils.data.DataLoader(apples_test_dataset,
                                             batch_size=batch_size,
                                             shuffle=True)
oranges_test_dl = torch.utils.data.DataLoader(oranges_test_dataset,
                                              batch_size=batch_size,
                                              shuffle=True)
 
# 创建模型
class Downsample(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Downsample, self).__init__()
        self.conv_relu = nn.Sequential(
                            nn.Conv2d(in_channels, out_channels,
                                      kernel_size=3, stride=2, padding=1),
                            nn.LeakyReLU(inplace=True),
            )
        self.bn = nn.InstanceNorm2d(out_channels)
    def forward(self, x, is_bn=True):
 
            x = self.conv_relu(x)
            if is_bn:
                x = self.bn(x)
            return x
 
 
 
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
        self.bn = nn.InstanceNorm2d(out_channels)
 
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
 
# 定义判别器
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.down1 = Downsample(3, 64)             # 128
        self.down2 = Downsample(64, 128)           # 64
        self.last = nn.Conv2d(128, 1, 3)
 
    def forward(self, img):
        x = self.down1(img)
        x = self.down2(x)
        x = torch.sigmoid(self.last(x))
        return x
 
device = "cuda" if torch.cuda.is_available() else "cpu"
gen_AB = Generator().to(device)
gen_BA = Generator().to(device)
dis_A = Discriminator().to(device)
dis_B = Discriminator().to(device)
 
 
bceloss_fn = torch.nn.BCELoss()                   # 定义损失函数
l1loss_fn = torch.nn.L1Loss()
# 同时对两个生成器进行优化
gen_optimizer = torch.optim.Adam(itertools.chain(gen_AB.parameters(), gen_BA.parameters()),
                                 lr=2e-4, betas=(0.5, 0.999))
dis_A_optimizer = torch.optim.Adam(dis_A.parameters(), lr=2e-4, betas=(0.5, 0.999))
dis_B_optimizer = torch.optim.Adam(dis_B.parameters(), lr=2e-4, betas=(0.5, 0.999))
 
def generate_images(model, test_input):
    prediction = model(test_input).permute(0, 2, 3, 1).detach().cpu().numpy()
    test_input = test_input.permute(0, 2, 3, 1).cpu().numpy()
    plt.figure(figsize=(10, 6))
    display_list = [test_input[0], prediction[0]]
    title = ['Input Image', 'Genrated Image']
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.title(title[i])
        plt.imshow(display_list[i] * 0.5 + 0.5)  # 转换到0-1
        plt.axis('off')
    plt.show()
 
test_batch = next(iter(apples_test_dl))
test_input = torch.unsqueeze(test_batch[0], 0).to(device)
 
D_loss = []  # 记录训练过程中判别器loss变化
G_loss = []  # 记录训练过程中生成器loss变化
 
# 开始训练
for epoch in range(50):
    D_epoch_loss = 0
    G_epoch_loss = 0
    for step, (real_A, real_B) in enumerate(zip(apples_dl, oranges_dl)):
        real_A = real_A.to(device)
        real_B = real_B.to(device)
 
        # GAN 训练
        gen_optimizer.zero_grad()
 
        # identity loss
        same_B = gen_AB(real_B)
        identity_B_loss = l1loss_fn(same_B, real_B)
        same_A = gen_BA(real_A)
        identity_A_loss = l1loss_fn(same_A, real_A)
 
        # GAN loss
        fake_B = gen_AB(real_A)
        D_pred_fake_B = dis_B(fake_B)
        gan_loss_AB = bceloss_fn(D_pred_fake_B,
                                 torch.ones_like(D_pred_fake_B, device=device))
 
        fake_A = gen_BA(real_B)
        D_pred_fake_A = dis_A(fake_A)
        gan_loss_BA = bceloss_fn(D_pred_fake_A,
                                 torch.ones_like(D_pred_fake_A, device=device))
 
        # cycle consistanse loss
        recovered_A = gen_BA(fake_B)
        cycle_loss_ABA = l1loss_fn(recovered_A, real_A)
 
        recovered_B = gen_AB(fake_A)
        cycle_loss_BAB = l1loss_fn(recovered_B, real_B)
 
        # total_loss
        g_loss = (identity_B_loss + identity_A_loss + gan_loss_AB + gan_loss_BA
                  + cycle_loss_ABA + cycle_loss_BAB)
 
        g_loss.backward()
        gen_optimizer.step()
 
        # dis_A 训练
        dis_A_optimizer.zero_grad()
        dis_A_real_output = dis_A(real_A)  # 判别器输入真实图片
        dis_A_real_loss = bceloss_fn(dis_A_real_output,
                                     torch.ones_like(dis_A_real_output, device=device))
 
        dis_A_fake_output = dis_A(fake_A.detach())  # 判别器输入生成图片
        dis_A_fake_loss = bceloss_fn(dis_A_fake_output,
                                     torch.zeros_like(dis_A_fake_output, device=device))
 
        dis_A_loss = (dis_A_real_loss + dis_A_fake_loss) * 0.5
 
        dis_A_loss.backward()
        dis_A_optimizer.step()
 
        # dis_B 训练
        dis_B_optimizer.zero_grad()
        dis_B_real_output = dis_B(real_B)  # 判别器输入真实图片
        dis_B_real_loss = bceloss_fn(dis_B_real_output,
                                     torch.ones_like(dis_B_real_output, device=device))
 
        dis_B_fake_output = dis_B(fake_B.detach())  # 判别器输入生成图片
        dis_B_fake_loss = bceloss_fn(dis_B_fake_output,
                                     torch.zeros_like(dis_B_fake_output, device=device))
 
        dis_B_loss = (dis_B_real_loss + dis_B_fake_loss) * 0.5
 
        dis_B_loss.backward()
        dis_B_optimizer.step()
 
        # 打印 loss 变化
        with torch.no_grad():
            D_epoch_loss += (dis_A_loss + dis_B_loss).item()
            G_epoch_loss += g_loss.item()
    with torch.no_grad():
        D_epoch_loss /= (step+1)
        G_epoch_loss /= (step+1)
        D_loss.append(D_epoch_loss)
        G_loss.append(G_epoch_loss)
        # 训练完一个Epoch，打印提示并绘制生成的图片
        print("Epoch:", epoch, "D_epoch_loss:", D_epoch_loss, "G_epoch_loss:", G_epoch_loss)
        generate_images(gen_AB, test_input)