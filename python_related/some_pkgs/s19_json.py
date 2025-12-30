"""
json - JSON编码和解码

json模块提供了JSON数据的编码(dumps)和解码(loads)功能。
官方文档: https://docs.python.org/3/library/json.html
"""

import json
from datetime import datetime
from decimal import Decimal


def example_basic_usage():
    """基本用法"""
    print("=" * 50)
    print("1. 基本用法")
    print("=" * 50)
    
    # Python对象 -> JSON字符串（编码/序列化）
    data = {
        'name': '张三',
        'age': 25,
        'city': '北京',
        'is_student': False,
        'scores': [85, 90, 78]
    }
    json_str = json.dumps(data)
    print(f"JSON字符串: {json_str}")
    
    # JSON字符串 -> Python对象（解码/反序列化）
    parsed_data = json.loads(json_str)
    print(f"Python对象: {parsed_data}")
    print(f"类型: {type(parsed_data)}")
    print()


def example_pretty_print():
    """格式化输出"""
    print("=" * 50)
    print("2. 格式化输出")
    print("=" * 50)
    
    data = {
        'name': '张三',
        'age': 25,
        'address': {
            'city': '北京',
            'street': '长安街'
        },
        'hobbies': ['读书', '旅游', '编程']
    }
    
    # 紧凑格式
    compact = json.dumps(data)
    print("紧凑格式:")
    print(compact)
    
    # 美化格式（缩进4空格）
    pretty = json.dumps(data, indent=4, ensure_ascii=False)
    print("\n美化格式:")
    print(pretty)
    
    # 自定义分隔符
    custom = json.dumps(data, indent=2, separators=(',', ': '), ensure_ascii=False)
    print("\n自定义分隔符:")
    print(custom)
    print()


def example_file_operations():
    """文件操作"""
    print("=" * 50)
    print("3. 文件操作")
    print("=" * 50)
    
    data = {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
        ],
        'total': 2
    }
    
    # 写入JSON文件
    with open('/tmp/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("数据已写入 /tmp/data.json")
    
    # 读取JSON文件
    with open('/tmp/data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    print(f"从文件读取的数据: {loaded_data}")
    print()


def example_data_types():
    """数据类型映射"""
    print("=" * 50)
    print("4. 数据类型映射")
    print("=" * 50)
    
    # Python -> JSON 类型映射
    python_data = {
        'string': 'hello',
        'integer': 42,
        'float': 3.14,
        'boolean': True,
        'none': None,
        'list': [1, 2, 3],
        'dict': {'key': 'value'}
    }
    
    json_str = json.dumps(python_data, indent=2)
    print("Python类型 -> JSON类型:")
    print(json_str)
    
    # JSON -> Python 类型映射
    print("\nJSON类型 -> Python类型:")
    print("  JSON object -> dict")
    print("  JSON array -> list")
    print("  JSON string -> str")
    print("  JSON number (int) -> int")
    print("  JSON number (real) -> float")
    print("  JSON true -> True")
    print("  JSON false -> False")
    print("  JSON null -> None")
    print()


def example_custom_encoder():
    """自定义编码器"""
    print("=" * 50)
    print("5. 自定义编码器")
    print("=" * 50)
    
    # 自定义编码器类
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)
    
    data = {
        'name': '订单',
        'created_at': datetime.now(),
        'price': Decimal('99.99')
    }
    
    # 使用自定义编码器
    json_str = json.dumps(data, cls=DateTimeEncoder, indent=2)
    print("使用自定义编码器:")
    print(json_str)
    print()


def example_custom_decoder():
    """自定义解码器"""
    print("=" * 50)
    print("6. 自定义解码器")
    print("=" * 50)
    
    json_str = '''
    {
        "name": "订单",
        "created_at": "2024-01-01T12:00:00",
        "price": "99.99"
    }
    '''
    
    # 自定义对象钩子
    def datetime_decoder(dct):
        for key, value in dct.items():
            if key.endswith('_at') and isinstance(value, str):
                try:
                    dct[key] = datetime.fromisoformat(value)
                except:
                    pass
            elif key == 'price' and isinstance(value, str):
                dct[key] = Decimal(value)
        return dct
    
    data = json.loads(json_str, object_hook=datetime_decoder)
    print("使用自定义解码器:")
    print(f"名称: {data['name']}")
    print(f"创建时间: {data['created_at']} (类型: {type(data['created_at'])})")
    print(f"价格: {data['price']} (类型: {type(data['price'])})")
    print()


def example_special_cases():
    """特殊情况处理"""
    print("=" * 50)
    print("7. 特殊情况处理")
    print("=" * 50)
    
    # 处理中文字符
    chinese_data = {'message': '你好，世界！'}
    
    # 默认会转义为ASCII
    ascii_json = json.dumps(chinese_data)
    print(f"ASCII编码: {ascii_json}")
    
    # 保留中文
    utf8_json = json.dumps(chinese_data, ensure_ascii=False)
    print(f"UTF-8编码: {utf8_json}")
    
    # 处理循环引用（会报错）
    # circular_data = {'key': None}
    # circular_data['key'] = circular_data
    # json.dumps(circular_data)  # 这会抛出 ValueError
    
    # 排序键
    unsorted = {'z': 1, 'a': 2, 'm': 3}
    sorted_json = json.dumps(unsorted, sort_keys=True)
    print(f"\n排序键: {sorted_json}")
    print()


def example_performance():
    """性能相关"""
    print("=" * 50)
    print("8. 性能相关")
    print("=" * 50)
    
    # 大数据示例
    large_data = [{'id': i, 'name': f'User{i}'} for i in range(1000)]
    
    import time
    
    # 序列化性能
    start = time.time()
    json_str = json.dumps(large_data)
    encode_time = time.time() - start
    print(f"序列化1000条记录耗时: {encode_time:.4f}秒")
    
    # 反序列化性能
    start = time.time()
    data = json.loads(json_str)
    decode_time = time.time() - start
    print(f"反序列化1000条记录耗时: {decode_time:.4f}秒")
    
    print(f"JSON字符串大小: {len(json_str)} 字节")
    print()


def example_validation():
    """JSON验证"""
    print("=" * 50)
    print("9. JSON验证")
    print("=" * 50)
    
    # 有效的JSON
    valid_json = '{"name": "Alice", "age": 25}'
    try:
        data = json.loads(valid_json)
        print(f"有效JSON: {data}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    
    # 无效的JSON
    invalid_json = "{'name': 'Alice', 'age': 25}"  # 使用单引号
    try:
        data = json.loads(invalid_json)
        print(f"有效JSON: {data}")
    except json.JSONDecodeError as e:
        print(f"无效JSON错误: {e}")
    
    # 尾随逗号（无效）
    trailing_comma = '{"name": "Alice", "age": 25,}'
    try:
        data = json.loads(trailing_comma)
        print(f"有效JSON: {data}")
    except json.JSONDecodeError as e:
        print(f"尾随逗号错误: {e}")
    print()


def example_nested_structures():
    """嵌套结构"""
    print("=" * 50)
    print("10. 嵌套结构")
    print("=" * 50)
    
    nested_data = {
        'company': '科技公司',
        'departments': [
            {
                'name': '研发部',
                'employees': [
                    {'id': 1, 'name': '张三', 'position': '工程师'},
                    {'id': 2, 'name': '李四', 'position': '架构师'}
                ]
            },
            {
                'name': '市场部',
                'employees': [
                    {'id': 3, 'name': '王五', 'position': '经理'}
                ]
            }
        ]
    }
    
    json_str = json.dumps(nested_data, indent=2, ensure_ascii=False)
    print("嵌套结构JSON:")
    print(json_str)
    
    # 访问嵌套数据
    data = json.loads(json_str)
    first_employee = data['departments'][0]['employees'][0]
    print(f"\n第一个员工: {first_employee['name']} - {first_employee['position']}")
    print()


def example_common_patterns():
    """常见模式"""
    print("=" * 50)
    print("11. 常见模式")
    print("=" * 50)
    
    # API响应格式
    api_response = {
        'status': 'success',
        'code': 200,
        'message': '操作成功',
        'data': {
            'user_id': 123,
            'username': 'alice'
        }
    }
    print("API响应格式:")
    print(json.dumps(api_response, indent=2, ensure_ascii=False))
    
    # 配置文件格式
    config = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'mydb'
        },
        'cache': {
            'enabled': True,
            'ttl': 300
        }
    }
    print("\n配置文件格式:")
    print(json.dumps(config, indent=2))
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("json库使用示例")
    print("=" * 50 + "\n")
    
    example_basic_usage()
    example_pretty_print()
    example_file_operations()
    example_data_types()
    example_custom_encoder()
    example_custom_decoder()
    example_special_cases()
    example_performance()
    example_validation()
    example_nested_structures()
    example_common_patterns()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
