from enum import Enum
import random

class UserRole(Enum):
    """
    包含 name 和 value 两个属性
    也可以通过字典创建动态enum
    """
    ADMIN = 67
    MODERATOR = 123
    USER = 89

def enum_usg():
    user_list = [e.name for e in UserRole]              # 获取所有枚举名称
    user_num_list = [e.value for e in UserRole]         # 获取所有枚举值
    
    # 1. 
    random_user = random.choice(user_list)              # 随机选择一个枚举名称
    # 正常都是 UserRole.ADMIN 这么用的
    
    # 2. 
    random_user_num = random.choice(user_num_list)      # 随机选择一个枚举值
    user = UserRole(random_user_num)                    # 根据枚举值获取对应的枚举
    print(f"{random_user_num} 的 name: {user.name}, value: {user.value}")
    pass

def enum_info():
    """查看enum"""
    print(UserRole)     # <enum 'UserRole'>
    # 遍历enum
    for role in UserRole:
        print(role)
        print(f"role name: {role.name}, role value: {role.value}")

def construct_enum():
    """通过字典创建动态enum"""
    a_dict = {"a": 1, "b": 2}
    aaa = Enum("ADict", a_dict)
    print(aaa)

def main():
    enum_info()
    construct_enum()
    enum_usg()
    pass


if __name__ == '__main__':
    main()