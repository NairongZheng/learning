- [总览](#总览)
- [super继承](#super继承)
- [pandas](#pandas)
- [loguru](#loguru)
- [re](#re)
- [PIL](#pil)
- [cv2](#cv2)


## 总览
1. s1_enum.py：枚举
2. s2_dataclass.py：数据类(装饰器实现)
3. s3_pydantic.py：数据验证和设置管理库
4. s4_namespace：命名空间
5. s5_pandas.py：pandas
6. s6_logging：日志库logging的使用
7. s7_loguru：日志库loguru的使用
8. s8_asyncio：协程
9. s9_bs：爬虫
10. s10_scikit-learn：机器学习与scikit-learn
11. s11_re.py：正则表达式
12. s12_PIL.py：PIL图像处理
13. s13_cv2.py：cv2图像处理
14. s14_fastapi：fastapi（还有例子可见[`python_related/connection/http_connect/fastapi_base/`](../connection/http_connect/fastapi_base/)）
15. s15_argparse.py：argparse
16. s16_tempfile.py：tempfile沙箱


## super继承
1. 基本用法
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的 __init__ 方法
        self.breed = breed

    def speak(self):
        super().speak()  # 调用父类的 speak 方法
        print("Dog barks")
```

2. 多重继承
```python
# 多重继承mro
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        super().method()
        print("Method in B")

class C(A):
    def method(self):
        super().method()
        print("Method in C")

class D(B, C):
    def method(self):
        super().method()
        print("Method in D")

if __name__ == '__main__:
    d = D()
    d.method()

    # # 输出
    # Method in A
    # Method in C
    # Method in B
    # Method in D
```


## pandas
1. `pd.read_csv`：读取csv为df
2. `df.sample`：打乱
3. `pd.concat`：拼接
4. `df.sort_index`：用index排序
5. `df.reset_index`：重新编号
6. `df.drop`：删除行或列
7. `df.groupby`：分组

## loguru
1. `logger.add`：添加新的日志处理器，可以将日志输出到不同的目的地，如文件、控制台、网络等，并配置其行为。一些参数如下：
   1. `sink`（必需）：指定日志的输出目标，例如，`"./logs/my_log.log"`将日志写入文件，`sys.stdout`将日志输出到控制台。
   2. `level`（可选）：指定要记录的最低日志级别，常用的级别有 `DEBUG, INFO, WARNING, ERROR, CRITICAL`。只记录该级别及以上的日志。
   3. `format`（可选）：自定义日志消息的格式，例如，`"{time} {level} {message}"` 可以指定日志中显示时间、级别和消息。
   4. `rotation`（可选）：指定日志文件的轮换策略。可以是时间（如 `"1 day"`）或文件大小（如 `"1 MB"`）。当日志达到指定条件时，会自动创建新的日志文件。
   5. `retention`（可选）：指定日志文件的保留策略。可以是时间（如 `"10 days"`）或文件数量（如 `5`）。超过这个限制的旧日志将被删除。
   6. `filter`（可选）：一个函数或字典，用于过滤哪些日志记录应该被处理。该过滤器接收一个 `record` 字典，返回布尔值。例如，`filter=lambda record: record["level"].name == "ERROR"` 只记录错误日志。
   7. `mode`（可选）：指定打开日志文件的模式，常用的有 `"w"`（写入，覆盖）和 `"a"`（追加）。
   8. `catch`（可选）：布尔值，指示是否捕获在日志记录时发生的异常。
2. `logger.bind`：返回一个新的 logger 对象，**该对象会自动将指定的上下文信息附加到日志消息中**。可以配合`logger.add`中的`filter`使用

## re
1. 常用方法：
   1. `re.match()`：用于从字符串的起始位置匹配一个模式，如果**起始位置**匹配成功，则返回匹配对象，否则返回None。
   2. `re.search()`：用于**扫描整个字符串，返回第一个匹配到的对象**。如果找不到匹配，则返回None。
   3. `re.findall()`：用于返回字符串中所有与模式匹配的子串，返回一个列表。
   4. `re.sub()`：用于替换字符串中所有匹配到的子串。可以通过正则表达式定义替换规则。
   5. `re.split()`：用于按照正则表达式匹配的子串分割字符串，返回一个列表。
2. 常用正则表达式符号：
   1. `.`：匹配任意字符（除了换行符）
   2. `^`：匹配字符串的开头
   3. `$`：匹配字符串的结尾
   4. `*`：匹配0个或多个前面的字符
   5. `+`：匹配1个或多个前面的字符（至少匹配一次且可以匹配多次）
   6. `?`：匹配0个或1个前面的字符
   7.  `\d`：匹配任何数字
   8.  `\w`：匹配字母、数字或下划线
   9.  `\s`：匹配空白字符
   10. `()`：小括号主要作用是捕获组和分组
      1.  捕获组：小括号可以将匹配到的子模式保存起来，便于后续引用或操作。匹配成功后，捕获组中的内容可以通过`\1`，`\2`等方式在正则表达式的替换部分或者后续代码中使用。
      2.  分组：小括号还能将模式的一部分视为一个整体，用于逻辑组合。例如，可以对一组模式使用量词（如+、*），让正则表达式更灵活。
   11. `[]`：中括号用于定义字符集，表示可以匹配其中的任意一个字符。中括号中的字符不会被解释为正则表达式的特殊符号，除了中括号本身、连字符（-）和反斜杠（\）。
   12. `{}`：大括号用于定义量词，指定前面的元素可以出现的次数。它允许你指定一个范围或确切的次数。
       1. `{n}`：匹配前面的字符n次
       2. `{n,m}`：匹配前面的字符n到m次

## PIL
1. 打开图片：`Image.open(path)`
2. 显示图片：`img.show()`
3. 获取信息：
   1. 尺寸（w, h）：`img.size`
   2. 模式（RGB、RGBA、L）：`img.mode`
   3. 格式（PNG、JEPG）：`img.format`
4. 调整大小：`img.resize((w, h))`
5. 裁剪：`img.crop((left, top, right, bottom))`
6. 旋转：`img.rotate(angle)`
7. 翻转：`img.transpose(Image.FLIP_LEFT_RIGHT)`
8. 颜色转换：`img.convert("L")`（灰度）
9.  调整亮度：`ImageEnhance.Brightness(img).enhance(value)`
10. 添加文本：`ImageDraw.Draw(img).text(position, text, fill, font)`
11. 保存图片：`img.save(filename, format, quality=value)`

## cv2
1. 读取图片：`cv2.imread(path, mode)`
2. 显示图片：`cv2.imshow("Window_name", img)`
3. 获取信息：
   1. 尺寸（h, w, c）：`img.shape`
   2. 像素总数：`img.size`
   3. 数据类型：`img.dtype`
4. 调整大小：`cv2.resize(img, (w, h))`
5. 裁剪：`img[y1:y2, x1:x2]`
6. 旋转：`cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)`
7. 翻转：`cv2.flip(img, 1)`
   1. 水平翻转：1
   2. 垂直翻转：0
   3. 水平垂直翻转：-1
8.  颜色转换：`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`
9.  画图：
    1.  画直线（起点, 终点, 颜色, 线宽）：`cv2.line(img, (50, 50), (200, 50), (0, 255, 0), 3)`
    2.  画矩形（左上角, 右下角, 颜色, 线宽）：`cv2.rectangle(img, (50, 50), (200, 150), (255, 0, 0), 3)`
    3.  画圆（圆心, 半径, 颜色, 线宽）：`cv2.circle(img, (150, 150), 50, (0, 0, 255), -1)`
10. 加文字（图片, 文字, 左上角, 字体, 字体大小, 颜色, 字体粗细）：`cv2.putText(img, "Hello, OpenCV!", (50, 200), font, 1, (0, 255, 255), 2)`
11. 保存图片：`cv2.imwrite("save_path", img)`
12. 模糊：`cv2.GaussianBlur()`
13. 边缘检测：`cv2.Canny()`
14. 读取视频：`cv2.VideoCapture()`