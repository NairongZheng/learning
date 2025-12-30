- [总览](#总览)
- [super继承](#super继承)
- [pandas](#pandas)
- [loguru](#loguru)
- [re](#re)
- [PIL](#pil)
- [cv2](#cv2)
- [requests](#requests)
- [pathlib](#pathlib)
- [json](#json)
- [datetime](#datetime)
- [collections](#collections)
- [itertools](#itertools)


## 总览

### 数据处理
1. s1_enum.py：枚举
2. s2_dataclass.py：数据类(装饰器实现)
3. s3_pydantic.py：数据验证和设置管理库
4. s4_namespace：命名空间
5. s5_pandas.py：pandas数据分析

### 日志系统
6. s6_logging：日志库logging的使用
7. s7_loguru：日志库loguru的使用（推荐）

### 异步编程
8. s8_asyncio：协程与异步编程

### 网络爬虫
9. s9_bs：BeautifulSoup爬虫

### 机器学习
10. s10_scikit-learn：机器学习与scikit-learn

### 文本与图像处理
11. s11_re.py：正则表达式
12. s12_PIL.py：PIL图像处理
13. s13_cv2.py：OpenCV图像处理

### Web框架
14. s14_fastapi：FastAPI Web框架（还有例子可见[`python_related/connection/http_connect/fastapi_base/`](../connection/http_connect/fastapi_base/)）

### 工具类
15. s15_argparse.py：命令行参数解析
16. s16_tempfile.py：临时文件处理
17. s17_requests.py：HTTP请求库
18. s18_pathlib.py：现代路径处理
19. s19_json.py：JSON操作
20. s20_datetime.py：日期时间处理
21. s21_collections.py：特殊数据结构（Counter、defaultdict、deque等）
22. s22_itertools.py：迭代器工具


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
## requests
HTTP请求库，简单优雅的HTTP客户端。
1. GET请求：`requests.get(url, params=params, headers=headers)`
2. POST请求：`requests.post(url, data=data, json=json_data)`
3. 其他方法：`requests.put()`, `requests.delete()`, `requests.patch()`
4. 响应对象：
   1. `response.status_code`：状态码
   2. `response.text`：文本内容
   3. `response.json()`：JSON数据
   4. `response.content`：二进制内容
   5. `response.headers`：响应头
5. Session：`session = requests.Session()`，保持会话状态
6. 超时设置：`timeout=3`
7. 文件上传：`files={'file': open('file.txt', 'rb')}`
8. 异常处理：`requests.exceptions.RequestException`

## pathlib
面向对象的文件系统路径操作，比os.path更现代。
1. 创建路径：`Path('/home/user/file.txt')`
2. 路径拼接：`path / 'subdir' / 'file.txt'`
3. 当前目录：`Path.cwd()`
4. 用户目录：`Path.home()`
5. 路径组成：
   1. `path.parent`：父目录
   2. `path.name`：文件名
   3. `path.stem`：文件名（不含扩展名）
   4. `path.suffix`：扩展名
6. 文件操作：
   1. `path.read_text()`：读取文本
   2. `path.write_text(content)`：写入文本
   3. `path.exists()`：检查是否存在
   4. `path.is_file()`：是否是文件
   5. `path.is_dir()`：是否是目录
7. 目录操作：
   1. `path.mkdir(parents=True)`：创建目录
   2. `path.iterdir()`：遍历目录
   3. `path.glob('*.txt')`：模式匹配
   4. `path.rglob('*.txt')`：递归匹配

## json
JSON编码和解码。
1. 序列化：
   1. `json.dumps(obj)`：对象转JSON字符串
   2. `json.dump(obj, file)`：对象写入文件
2. 反序列化：
   1. `json.loads(str)`：JSON字符串转对象
   2. `json.load(file)`：从文件读取JSON
3. 常用参数：
   1. `indent=4`：美化输出
   2. `ensure_ascii=False`：保留中文
   3. `sort_keys=True`：排序键
4. 自定义编码：`json.dumps(obj, cls=CustomEncoder)`
5. 数据类型映射：
   1. Python dict ↔ JSON object
   2. Python list ↔ JSON array
   3. Python str ↔ JSON string
   4. Python int/float ↔ JSON number
   5. Python True/False ↔ JSON true/false
   6. Python None ↔ JSON null

## datetime
日期和时间处理。
1. 创建：
   1. `datetime.now()`：当前日期时间
   2. `date.today()`：当前日期
   3. `datetime(2024, 12, 25, 15, 30)`：指定日期时间
2. 格式化：
   1. `dt.strftime('%Y-%m-%d %H:%M:%S')`：格式化输出
   2. `datetime.strptime(str, format)`：解析字符串
3. 时间差：
   1. `timedelta(days=7, hours=3)`：创建时间差
   2. `dt1 - dt2`：计算差值
   3. `dt + timedelta(...)`：日期运算
4. 组成部分：`year`, `month`, `day`, `hour`, `minute`, `second`
5. 时区：`datetime.now(timezone.utc)`
6. 时间戳：`dt.timestamp()`，`datetime.fromtimestamp(ts)`

## collections
特殊容器数据类型。
1. `Counter`：计数器
   1. `Counter(list)`：统计元素出现次数
   2. `most_common(n)`：最常见的n个元素
2. `defaultdict`：带默认值的字典
   1. `defaultdict(list)`：默认值为空列表
   2. `defaultdict(int)`：默认值为0
3. `deque`：双端队列
   1. `append(x)`：右端添加
   2. `appendleft(x)`：左端添加
   3. `pop()`：右端弹出
   4. `popleft()`：左端弹出
4. `namedtuple`：命名元组
   1. `Point = namedtuple('Point', ['x', 'y'])`
   2. 可以通过名称访问字段
5. `OrderedDict`：有序字典（Python 3.7+普通dict也有序）
6. `ChainMap`：链式字典，多个字典的视图

## itertools
迭代器工具，高效的迭代器函数。
1. 无限迭代器：
   1. `count(start, step)`：无限计数
   2. `cycle(iterable)`：无限循环
   3. `repeat(elem, n)`：重复元素
2. 终止迭代器：
   1. `chain(*iterables)`：连接多个可迭代对象
   2. `compress(data, selectors)`：根据选择器过滤
   3. `islice(iterable, stop)`：切片
   4. `accumulate(iterable)`：累积操作
3. 组合迭代器：
   1. `product(*iterables)`：笛卡尔积
   2. `permutations(iterable, r)`：排列
   3. `combinations(iterable, r)`：组合
4. 其他：
   1. `groupby(iterable, key)`：分组
   2. `zip_longest(*iterables)`：长度不等的zip
   3. `starmap(func, iterable)`：解包参数映射
