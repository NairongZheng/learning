import os
import pathlib
import numpy as np
import cv2


proj_path = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
img_file = os.path.join(proj_path, "img")
raw_img_path = os.path.join(img_file, "PIL_and_cv2_raw_img.png")


class Cv2Test:
    def __init__(self):
        self.raw_img_path = raw_img_path
        self.img = self.read_img()
    
    def read_img(self):
        img = cv2.imread(self.raw_img_path)
        return img
    
    def show_img(self, img):
        cv2.imshow("show_image", img)
        # 等待按键并关闭窗口
        cv2.waitKey(0)
        # cv2.destroyWindow("show_image")
        cv2.destroyAllWindows()
    
    def get_img_msg(self):
        img_shape = self.img.shape
        img_size = self.img.size
        img_dtye = self.img.dtype
        print(f"Cv2Test img_shape: {img_shape}") # (高, 宽, 通道数)
        print(f"Cv2Test img_size: {img_size}") # 像素总数
        print(f"Cv2Test img_dtye: {img_dtye}") # 数据类型
    
    def resize_img(self):
        raw_size = self.img.shape
        new_h = int(raw_size[0] * 0.5)
        new_w = int(raw_size[1] * 0.3)
        img_resized = cv2.resize(self.img, (new_w, new_h))
        print(f"Cv2Test new_size: {img_resized.shape}")
        # self.show_img(img_resized)
    
    def cut_img(self):
        img_cropped = self.img[50:200, 50:200] # 裁剪出 (50,50) 到 (200,200) 之间的区域
        # self.show_img(img_cropped)
    
    def rotate_img(self):
        img_rotated = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE) # 旋转
        # self.show_img(img_rotated)
        img_flipped = cv2.flip(self.img, 1) # 水平翻转，0是垂直翻转，1是水平翻转，-1是水平垂直翻转
        # self.show_img(img_flipped)
    
    def convert_img(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY) # 转换成灰度图
        # self.show_img(gray)
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV) # 转换为HSV颜色空间
        # self.show_img(hsv)
    
    def draw_img(self):
        img_drawed = self.img.copy()
        cv2.line(img_drawed, (50, 50), (200, 200), (0, 0, 0), 3)
        cv2.rectangle(img_drawed, (50, 50), (200, 150), (255, 0, 0), 3)
        cv2.circle(img_drawed, (150, 150), 50, (0, 0, 255), 3) # -1就是填满实心圆
        # self.show_img(img_drawed)
    
    def text_img(self):
        img_texted = self.img.copy()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_texted, "Hello, OpenCV!", (50, 200), font, 1, (0, 255, 255), 2)
        self.show_img(img_texted)
    
    def test(self):
        # self.show_img(self.img)
        self.get_img_msg()
        self.resize_img()
        self.cut_img()
        self.rotate_img()
        self.convert_img()
        self.draw_img()
        self.text_img()
        pass


def main():
    cv2_test = Cv2Test()
    cv2_test.test()
    pass


if __name__ == "__main__":
    main()
