"""
collections - 特殊数据结构

collections模块提供了多种特殊的容器数据类型。
官方文档: https://docs.python.org/3/library/collections.html
"""

from collections import (
    Counter, defaultdict, OrderedDict, deque,
    namedtuple, ChainMap
)


def example_counter():
    """Counter - 计数器"""
    print("=" * 50)
    print("1. Counter - 计数器")
    print("=" * 50)
    
    # 创建Counter
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    counter = Counter(words)
    print(f"计数结果: {counter}")
    
    # 访问计数
    print(f"apple出现次数: {counter['apple']}")
    print(f"grape出现次数: {counter['grape']}")  # 不存在返回0
    
    # 字符串计数
    text = "abracadabra"
    char_counter = Counter(text)
    print(f"\n字符计数: {char_counter}")
    
    # 最常见的元素
    print(f"最常见的3个: {char_counter.most_common(3)}")
    
    # Counter运算
    c1 = Counter(['a', 'b', 'c', 'a'])
    c2 = Counter(['a', 'b', 'd'])
    print(f"\nCounter加法: {c1 + c2}")
    print(f"Counter减法: {c1 - c2}")
    print(f"Counter交集: {c1 & c2}")
    print(f"Counter并集: {c1 | c2}")
    
    # 更新计数
    counter.update(['apple', 'grape'])
    print(f"\n更新后: {counter}")
    
    # 获取所有元素
    print(f"所有元素: {list(counter.elements())[:10]}")
    print()


def example_defaultdict():
    """defaultdict - 带默认值的字典"""
    print("=" * 50)
    print("2. defaultdict - 带默认值的字典")
    print("=" * 50)
    
    # 创建defaultdict - list类型
    dd_list = defaultdict(list)
    dd_list['fruits'].append('apple')
    dd_list['fruits'].append('banana')
    dd_list['vegetables'].append('carrot')
    print(f"list类型: {dict(dd_list)}")
    
    # int类型（计数）
    dd_int = defaultdict(int)
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    for word in words:
        dd_int[word] += 1
    print(f"\nint类型计数: {dict(dd_int)}")
    
    # set类型
    dd_set = defaultdict(set)
    data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
    for category, item in data:
        dd_set[category].add(item)
    print(f"\nset类型: {dict(dd_set)}")
    
    # lambda默认值
    dd_lambda = defaultdict(lambda: 'N/A')
    dd_lambda['name'] = 'Alice'
    print(f"\nlambda默认值:")
    print(f"  name: {dd_lambda['name']}")
    print(f"  age: {dd_lambda['age']}")  # 返回N/A
    
    # 嵌套defaultdict
    nested_dd = defaultdict(lambda: defaultdict(int))
    nested_dd['user1']['score'] = 100
    nested_dd['user1']['level'] = 5
    print(f"\n嵌套defaultdict: {dict(nested_dd)}")
    print()


def example_ordereddict():
    """OrderedDict - 有序字典（注意：Python 3.7+普通dict也保持插入顺序）"""
    print("=" * 50)
    print("3. OrderedDict - 有序字典")
    print("=" * 50)
    
    # 创建OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    print(f"OrderedDict: {od}")
    
    # 移动到末尾
    od.move_to_end('a')
    print(f"移动'a'到末尾: {od}")
    
    # 移动到开头
    od.move_to_end('c', last=False)
    print(f"移动'c'到开头: {od}")
    
    # 弹出最后一个
    last_item = od.popitem(last=True)
    print(f"弹出最后一个: {last_item}, 剩余: {od}")
    
    # 弹出第一个
    first_item = od.popitem(last=False)
    print(f"弹出第一个: {first_item}, 剩余: {od}")
    
    # 相等性比较（考虑顺序）
    od1 = OrderedDict([('a', 1), ('b', 2)])
    od2 = OrderedDict([('b', 2), ('a', 1)])
    print(f"\nod1 == od2: {od1 == od2}")  # False，顺序不同
    
    # 普通dict比较（不考虑顺序）
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 2, 'a': 1}
    print(f"d1 == d2: {d1 == d2}")  # True
    print()


def example_deque():
    """deque - 双端队列"""
    print("=" * 50)
    print("4. deque - 双端队列")
    print("=" * 50)
    
    # 创建deque
    dq = deque([1, 2, 3])
    print(f"初始deque: {dq}")
    
    # 右端添加
    dq.append(4)
    print(f"右端添加4: {dq}")
    
    # 左端添加
    dq.appendleft(0)
    print(f"左端添加0: {dq}")
    
    # 右端弹出
    right = dq.pop()
    print(f"右端弹出{right}: {dq}")
    
    # 左端弹出
    left = dq.popleft()
    print(f"左端弹出{left}: {dq}")
    
    # 扩展
    dq.extend([5, 6])
    print(f"右端扩展[5,6]: {dq}")
    
    dq.extendleft([-1, -2])  # 注意：会反转
    print(f"左端扩展[-1,-2]: {dq}")
    
    # 旋转
    dq.rotate(2)  # 向右旋转
    print(f"向右旋转2位: {dq}")
    
    dq.rotate(-3)  # 向左旋转
    print(f"向左旋转3位: {dq}")
    
    # 限制长度的deque
    limited_dq = deque(maxlen=3)
    for i in range(5):
        limited_dq.append(i)
        print(f"添加{i}, 当前deque: {limited_dq}")
    
    # 使用场景：滑动窗口
    print("\n滑动窗口示例:")
    window = deque(maxlen=3)
    data = [1, 2, 3, 4, 5, 6]
    for num in data:
        window.append(num)
        if len(window) == 3:
            print(f"  窗口: {list(window)}, 平均值: {sum(window)/3:.1f}")
    print()


def example_namedtuple():
    """namedtuple - 命名元组"""
    print("=" * 50)
    print("5. namedtuple - 命名元组")
    print("=" * 50)
    
    # 创建命名元组类
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"点坐标: {p}")
    print(f"x坐标: {p.x}")
    print(f"y坐标: {p.y}")
    print(f"索引访问: p[0]={p[0]}, p[1]={p[1]}")
    
    # 使用字符串创建
    Person = namedtuple('Person', 'name age city')
    person = Person('Alice', 25, 'Beijing')
    print(f"\n人员信息: {person}")
    print(f"姓名: {person.name}")
    
    # 从可迭代对象创建
    data = ['Bob', 30, 'Shanghai']
    person2 = Person._make(data)
    print(f"从列表创建: {person2}")
    
    # 转换为字典
    print(f"转为字典: {person._asdict()}")
    
    # 替换字段（返回新对象）
    person3 = person._replace(age=26)
    print(f"替换年龄: {person3}")
    
    # 默认值
    Employee = namedtuple('Employee', ['name', 'department', 'salary'], defaults=['Unknown', 0])
    emp1 = Employee('Charlie')
    print(f"\n带默认值: {emp1}")
    
    # 使用场景：返回多个值
    def get_user_info():
        User = namedtuple('User', ['id', 'name', 'email'])
        return User(1, 'Alice', 'alice@example.com')
    
    user = get_user_info()
    print(f"\n函数返回: id={user.id}, name={user.name}, email={user.email}")
    print()


def example_chainmap():
    """ChainMap - 链式字典"""
    print("=" * 50)
    print("6. ChainMap - 链式字典")
    print("=" * 50)
    
    # 创建ChainMap
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'c': 5, 'd': 6}
    
    chain = ChainMap(dict1, dict2, dict3)
    print(f"ChainMap: {chain}")
    print(f"所有键: {list(chain.keys())}")
    print(f"所有值: {list(chain.values())}")
    
    # 查找顺序（从左到右）
    print(f"\n查找'a': {chain['a']}")  # 来自dict1
    print(f"查找'b': {chain['b']}")  # 来自dict1（不是dict2）
    print(f"查找'c': {chain['c']}")  # 来自dict2（不是dict3）
    print(f"查找'd': {chain['d']}")  # 来自dict3
    
    # 修改（只影响第一个字典）
    chain['a'] = 10
    print(f"\n修改后dict1: {dict1}")
    
    # 添加新字典
    dict4 = {'e': 7}
    chain = chain.new_child(dict4)
    print(f"\n添加新字典: {chain}")
    print(f"查找'e': {chain['e']}")
    
    # 移除最前面的字典
    chain = chain.parents
    print(f"移除最前面: {chain}")
    
    # 使用场景：配置管理
    defaults = {'theme': 'light', 'language': 'en', 'font_size': 12}
    user_config = {'theme': 'dark', 'font_size': 14}
    
    config = ChainMap(user_config, defaults)
    print(f"\n配置系统:")
    print(f"  theme: {config['theme']}")  # 使用用户配置
    print(f"  language: {config['language']}")  # 使用默认配置
    print(f"  font_size: {config['font_size']}")  # 使用用户配置
    print()


def example_practical_examples():
    """实用示例"""
    print("=" * 50)
    print("7. 实用示例")
    print("=" * 50)
    
    # 1. 使用Counter统计词频
    text = "the quick brown fox jumps over the lazy dog the fox"
    word_freq = Counter(text.split())
    print(f"词频统计: {word_freq.most_common(3)}")
    
    # 2. 使用defaultdict分组
    students = [
        ('Alice', 'Math'),
        ('Bob', 'English'),
        ('Charlie', 'Math'),
        ('David', 'English'),
        ('Eve', 'Math')
    ]
    
    groups = defaultdict(list)
    for name, subject in students:
        groups[subject].append(name)
    print(f"\n学生分组:")
    for subject, names in groups.items():
        print(f"  {subject}: {names}")
    
    # 3. 使用deque实现LRU缓存
    class LRUCache:
        def __init__(self, capacity):
            self.cache = {}
            self.queue = deque()
            self.capacity = capacity
        
        def get(self, key):
            if key in self.cache:
                self.queue.remove(key)
                self.queue.append(key)
                return self.cache[key]
            return None
        
        def put(self, key, value):
            if key in self.cache:
                self.queue.remove(key)
            elif len(self.cache) >= self.capacity:
                oldest = self.queue.popleft()
                del self.cache[oldest]
            
            self.cache[key] = value
            self.queue.append(key)
    
    cache = LRUCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    print(f"\nLRU缓存演示:")
    print(f"  get('a'): {cache.get('a')}")
    cache.put('c', 3)  # 淘汰'b'
    print(f"  get('b'): {cache.get('b')}")  # None
    print(f"  get('c'): {cache.get('c')}")
    
    # 4. 使用namedtuple处理CSV数据
    Book = namedtuple('Book', ['title', 'author', 'year'])
    books = [
        Book('Python入门', '张三', 2020),
        Book('数据结构', '李四', 2019),
        Book('算法导论', '王五', 2021)
    ]
    print(f"\n图书列表:")
    for book in books:
        print(f"  {book.title} - {book.author} ({book.year})")
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("collections库使用示例")
    print("=" * 50 + "\n")
    
    example_counter()
    example_defaultdict()
    example_ordereddict()
    example_deque()
    example_namedtuple()
    example_chainmap()
    example_practical_examples()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
