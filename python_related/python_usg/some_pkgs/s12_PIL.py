import os
import pathlib
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageFont


proj_path = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
img_file = os.path.join(proj_path, "img")
raw_img_path = os.path.join(img_file, "PIL_and_cv2_raw_img.png")


class PILTest:
    def __init__(self):
        self.raw_img_path = raw_img_path
        self.img = self.read_img()
        pass
    
    def read_img(self):
        img = Image.open(self.raw_img_path)
        return img
    
    def show_img(self, img: Image):
        img.show()
    
    def get_img_msg(self):
        img_size = self.img.size # (w, h)
        img_mode = self.img.mode
        img_format = self.img.format
        print(f"PILTest img_size: {img_size}")
        print(f"PILTest img_mode: {img_mode}")
        print(f"PILTest img_format: {img_format}")
    
    def resize_img(self):
        raw_size = self.img.size
        new_w = int(raw_size[0] * 0.5)
        new_h = int(raw_size[1] * 0.3)
        img_resized = self.img.resize((new_w, new_h))
        print(f"PILTest new_size: {img_resized.size}")
        # self.show_img(img_resized)
    
    def cut_img(self):
        # 裁剪区域 (左, 上, 右, 下)
        box = (50, 50, 200, 200)
        img_cropped = self.img.crop(box)
        # self.show_img(img_cropped)
    
    def rotate_img(self):
        angle = 45
        img_rotated = self.img.rotate(angle) # 旋转
        # self.show_img(img_rotated)
        img_filpped = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        # self.show_img(img_filpped)
    
    def convert_img(self):
        img_gray = self.img.convert("L") # 转换成灰度图
        # self.show_img(img_gray)
        img_rgba = self.img.convert("RGBA") # 转换成RGBA
        # self.show_img(img_rgba)
    
    def enhance_img(self):
        brighter_enhancer = ImageEnhance.Brightness(self.img) # 调整亮度（1.0为原始值，大则亮，小则暗）
        img_brighter = brighter_enhancer.enhance(1.5)
        # self.show_img(img_brighter)
        contrast_enhancer = ImageEnhance.Contrast(self.img) # 调整对比度
        img_contrast = contrast_enhancer.enhance(2.0)
        # self.show_img(img_contrast)
    
    def text_img(self):
        img_draw = self.img.copy()
        draw = ImageDraw.Draw(img_draw)
        font = ImageFont.load_default() # 选择字体
        draw.text((50, 50), "Hello, PIL", fill="red", font=font) # 在 (50, 50) 位置绘制文本
        # self.show_img(img_draw)
    
    def process_img(self):
        new_img = self.img.copy().convert("RGBA")
        data = new_img.getdata()
        new_data = [(r, g, b, int(a * 0.5)) for r, g, b, a in data]
        new_img.putdata(new_data)
        # self.show_img(new_img)
    
    def test(self):
        # self.show_img(self.img) # 显示图片
        self.get_img_msg() # 获取图片信息
        self.resize_img() # 调整图片大小
        self.cut_img() # 裁剪图片
        self.rotate_img() # 旋转和翻转
        self.convert_img() # 转换颜色模式
        self.enhance_img() # 调整亮度对比度
        self.text_img() # 在图片上绘制文本
        self.process_img() # 处理图片（调整透明度）
        pass


def main():
    pil_test = PILTest()
    pil_test.test()
    pass


if __name__ == "__main__":
    main()
