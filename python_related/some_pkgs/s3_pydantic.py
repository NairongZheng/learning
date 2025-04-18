"""
1. 数据模型：使用 BaseModel 创建数据模型。
2. 数据验证：当创建模型实例时，Pydantic 会自动验证输入数据。
3. 类型转换：Pydantic 支持将输入数据自动转换为指定类型。
4. 嵌套模型：支持嵌套数据模型。
5. 自定义验证：可以使用 @field_validator 装饰器自定义字段验证。（是有顺序的！！）
6. 序列化和反序列化：可以轻松地将模型实例转换为字典或 JSON 格式。
Pydantic 特别适用于 FastAPI 等框架，用于请求体和响应体的验证。它的类型安全性和直观的 API 使得数据处理变得简单且高效。
"""

from pydantic import BaseModel, field_validator, validator


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    confirm_password: str
    address: Address

    # 2.0版本弃用validator
    @validator('email')
    def email_must_contain_at(cls, v):
        if "@" not in v:
            raise ValueError("must contain @")
        return v

    @field_validator('confirm_password')
    def validate_passwords(cls, v, values):
        """
        cls: 这是类方法的第一个参数，代表当前的类（在这里是 User 类）。在方法中可以访问类的属性和方法。
        v: 这是当前字段（在这个例子中是 confirm_password）的值。在验证时传入的值。
        values: 存储了已经验证的字段的值！！！在字段验证时，你可以使用这个字典来访问其他字段的值，例如 password。
        """
        password = values.data.get('password')
        if password != v:
            raise ValueError('Passwords do not match')
        return v


def main():
    # 有一个错，password跟confirm_password不匹配
    user_1 = User(
        id=1,
        name="Alice",
        email="alice@example.com",
        password="secret",
        confirm_password="not_secret",
        address={"city": "Wonderland", "country": "Fantasy"},
    )
    # 有两个错，id不是int，password跟confirm_password不匹配
    user_2 = User(
        id="hashd",
        name="Alice",
        email="alice@example.com",
        password="secret",
        confirm_password="not_secret",
        address={"city": "Wonderland", "country": "Fantasy"},
    )
    pass


if __name__ == "__main__":
    main()
