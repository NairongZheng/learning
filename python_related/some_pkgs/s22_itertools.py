"""
itertools - 迭代器工具

itertools模块提供了用于创建高效迭代器的函数。
官方文档: https://docs.python.org/3/library/itertools.html
"""

import itertools
from itertools import (
    count, cycle, repeat, chain, compress, dropwhile, filterfalse,
    islice, starmap, takewhile, zip_longest, combinations,
    combinations_with_replacement, permutations, product,
    groupby, accumulate
)


def example_infinite_iterators():
    """无限迭代器"""
    print("=" * 50)
    print("1. 无限迭代器")
    print("=" * 50)
    
    # count - 从start开始无限计数
    print("count(10, 2): ", end="")
    for i in count(10, 2):
        if i > 20:
            break
        print(i, end=" ")
    print()
    
    # cycle - 无限循环可迭代对象
    print("cycle(['A', 'B', 'C']): ", end="")
    counter = 0
    for item in cycle(['A', 'B', 'C']):
        if counter >= 7:
            break
        print(item, end=" ")
        counter += 1
    print()
    
    # repeat - 重复一个值
    print("repeat('Hello', 3): ", end="")
    for item in repeat('Hello', 3):
        print(item, end=" ")
    print("\n")


def example_terminating_iterators():
    """终止迭代器"""
    print("=" * 50)
    print("2. 终止迭代器")
    print("=" * 50)
    
    # accumulate - 累积操作
    data = [1, 2, 3, 4, 5]
    print(f"原始数据: {data}")
    print(f"accumulate累加: {list(accumulate(data))}")
    print(f"accumulate累乘: {list(accumulate(data, lambda x, y: x * y))}")
    
    # chain - 连接多个可迭代对象
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [10, 20]
    print(f"\nchain连接: {list(chain(list1, list2, list3))}")
    
    # chain.from_iterable - 从可迭代对象的可迭代对象连接
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"chain.from_iterable展开: {list(chain.from_iterable(nested))}")
    
    # compress - 根据选择器过滤
    data = ['A', 'B', 'C', 'D', 'E']
    selectors = [1, 0, 1, 0, 1]
    print(f"\ncompress过滤: {list(compress(data, selectors))}")
    
    # dropwhile - 删除满足条件的元素直到条件不满足
    data = [1, 2, 3, 4, 5, 1, 2]
    print(f"dropwhile(x<4): {list(dropwhile(lambda x: x < 4, data))}")
    
    # takewhile - 保留满足条件的元素直到条件不满足
    print(f"takewhile(x<4): {list(takewhile(lambda x: x < 4, data))}")
    
    # filterfalse - 过滤不满足条件的元素（与filter相反）
    print(f"filterfalse(x<4): {list(filterfalse(lambda x: x < 4, data))}")
    
    # islice - 切片
    data = range(10)
    print(f"\nislice(data, 5): {list(islice(data, 5))}")  # 前5个
    print(f"islice(data, 2, 7): {list(islice(range(10), 2, 7))}")  # [2:7]
    print(f"islice(data, 1, 9, 2): {list(islice(range(10), 1, 9, 2))}")  # [1:9:2]
    print()


def example_combinatoric_iterators():
    """组合迭代器"""
    print("=" * 50)
    print("3. 组合迭代器")
    print("=" * 50)
    
    data = ['A', 'B', 'C']
    
    # product - 笛卡尔积
    print(f"product({data}, repeat=2):")
    for item in product(data, repeat=2):
        print(f"  {item}")
    
    # permutations - 排列（全排列）
    print(f"\npermutations({data}):")
    for item in permutations(data):
        print(f"  {item}")
    
    print(f"\npermutations({data}, 2):")
    for item in permutations(data, 2):
        print(f"  {item}")
    
    # combinations - 组合（无重复）
    print(f"\ncombinations({data}, 2):")
    for item in combinations(data, 2):
        print(f"  {item}")
    
    # combinations_with_replacement - 组合（可重复）
    print(f"\ncombinations_with_replacement({data}, 2):")
    for item in combinations_with_replacement(data, 2):
        print(f"  {item}")
    print()


def example_zip_longest():
    """zip_longest - 长度不等的zip"""
    print("=" * 50)
    print("4. zip_longest")
    print("=" * 50)
    
    list1 = [1, 2, 3]
    list2 = ['a', 'b']
    list3 = [10, 20, 30, 40]
    
    # 普通zip（截断到最短）
    print(f"普通zip: {list(zip(list1, list2, list3))}")
    
    # zip_longest（填充到最长）
    print(f"zip_longest: {list(zip_longest(list1, list2, list3))}")
    
    # 自定义填充值
    print(f"zip_longest(fillvalue=0): {list(zip_longest(list1, list2, list3, fillvalue=0))}")
    print()


def example_groupby():
    """groupby - 分组"""
    print("=" * 50)
    print("5. groupby - 分组")
    print("=" * 50)
    
    # 按相同值分组（需要先排序）
    data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
    print(f"原始数据: {data}")
    print("分组结果:")
    for key, group in groupby(data):
        print(f"  {key}: {list(group)}")
    
    # 按条件分组
    words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'cranberry']
    words.sort(key=lambda x: x[0])  # 按首字母排序
    print(f"\n单词列表: {words}")
    print("按首字母分组:")
    for key, group in groupby(words, key=lambda x: x[0]):
        print(f"  {key}: {list(group)}")
    
    # 按长度分组
    words = ['a', 'bb', 'ccc', 'dd', 'eee', 'f']
    print(f"\n单词列表: {words}")
    print("按长度分组:")
    for key, group in groupby(words, key=len):
        print(f"  长度{key}: {list(group)}")
    print()


def example_starmap():
    """starmap - 解包参数"""
    print("=" * 50)
    print("6. starmap - 解包参数")
    print("=" * 50)
    
    # 计算多个数的幂
    data = [(2, 3), (3, 2), (4, 2)]
    print(f"数据: {data}")
    print(f"starmap(pow): {list(starmap(pow, data))}")
    
    # 自定义函数
    def multiply(x, y):
        return x * y
    
    pairs = [(2, 3), (4, 5), (6, 7)]
    print(f"\n数据: {pairs}")
    print(f"starmap(multiply): {list(starmap(multiply, pairs))}")
    print()


def example_practical_examples():
    """实用示例"""
    print("=" * 50)
    print("7. 实用示例")
    print("=" * 50)
    
    # 1. 生成序列号
    print("生成序列号:")
    for i, num in zip(range(5), count(1000, 100)):
        print(f"  ID-{num}")
    
    # 2. 轮询服务器
    print("\n轮询服务器:")
    servers = ['server1', 'server2', 'server3']
    for i, server in zip(range(7), cycle(servers)):
        print(f"  请求{i+1} -> {server}")
    
    # 3. 批处理
    print("\n批处理数据:")
    data = range(10)
    batch_size = 3
    it = iter(data)
    while True:
        batch = list(islice(it, batch_size))
        if not batch:
            break
        print(f"  批次: {batch}")
    
    # 4. 滑动窗口
    print("\n滑动窗口:")
    def sliding_window(iterable, n):
        iterables = itertools.tee(iterable, n)
        for i, it in enumerate(iterables):
            for _ in range(i):
                next(it, None)
        return zip(*iterables)
    
    data = [1, 2, 3, 4, 5, 6]
    for window in sliding_window(data, 3):
        print(f"  窗口: {window}")
    
    # 5. 分页
    print("\n分页:")
    items = list(range(1, 21))
    page_size = 5
    for page_num, page_start in enumerate(range(0, len(items), page_size), 1):
        page = items[page_start:page_start + page_size]
        print(f"  第{page_num}页: {page}")
    
    # 6. 生成测试数据
    print("\n生成测试数据:")
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    cities = ['Beijing', 'Shanghai']
    for name, age, city in product(names[:2], ages[:2], cities[:1]):
        print(f"  {name}, {age}岁, {city}")
    
    # 7. 统计连续相同值的数量
    print("\n统计连续相同值:")
    data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    for key, group in groupby(data):
        print(f"  {key}: 连续{len(list(group))}次")
    
    # 8. 展平嵌套列表
    print("\n展平嵌套列表:")
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened = list(chain.from_iterable(nested))
    print(f"  嵌套: {nested}")
    print(f"  展平: {flattened}")
    
    # 9. 数据过滤和转换
    print("\n过滤偶数并累加:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filterfalse(lambda x: x % 2, numbers)
    cumsum = list(accumulate(even_numbers))
    print(f"  结果: {cumsum}")
    print()


def example_performance_tips():
    """性能提示"""
    print("=" * 50)
    print("8. 性能提示")
    print("=" * 50)
    
    # itertools比列表推导式更节省内存
    print("内存效率比较:")
    
    # 列表推导式（占用内存）
    list_comp = [x**2 for x in range(1000000)]
    print(f"  列表推导式创建了完整列表")
    
    # itertools（惰性求值）
    iter_map = map(lambda x: x**2, range(1000000))
    print(f"  itertools创建了迭代器（惰性求值）")
    
    # 只在需要时才计算
    print(f"  取前5个: {list(islice(iter_map, 5))}")
    
    print("\n组合爆炸警告:")
    print(f"  3个元素的全排列: {len(list(permutations([1,2,3])))} 个")
    print(f"  5个元素的全排列: {len(list(permutations([1,2,3,4,5])))} 个")
    print(f"  10个元素的全排列会有 3,628,800 个！")
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("itertools库使用示例")
    print("=" * 50 + "\n")
    
    example_infinite_iterators()
    example_terminating_iterators()
    example_combinatoric_iterators()
    example_zip_longest()
    example_groupby()
    example_starmap()
    example_practical_examples()
    example_performance_tips()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
