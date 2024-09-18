class MyContextManager:
    def __enter__(self):
        print("进入上下文")
        return self
        # 返回当前的上下文管理器对象（即 MyContextManager 的实例），这样可以在 with 语句中将其赋值给 as 后的变量（在这个例子中是 manager）。

    def __exit__(self, exc_type, exc_value, traceback):
        """
        当 with 块结束时，无论是否有异常，这个方法都会被调用。
        exc_type: 如果在 with 块中发生了异常，这个参数会包含异常的类型；否则，它的值为 None。
        exc_value: 如果有异常，这里是异常的实际值。
        traceback: 异常的追踪信息对象，可以提供详细的错误信息。
        """
        print("退出上下文")
        
        # 1. 可以返回 False 以继续抛出异常
        if exc_type:
            print(f"发生异常: {exc_value}")
            print(f"异常类型: {exc_type}")
            print(f"追踪信息: {traceback}")
            return False  # 返回 False 以继续抛出异常
        
        # # 2. 可以处理异常，返回 True 则不再抛出异常
        # if exc_type:
        #     print(f"已捕获异常: {exc_value}")
        #     return True  # 抑制异常


# 使用示例
try:
    with MyContextManager() as manager:
        print("在上下文中")
        raise ValueError("这是一个测试异常") # 如果返回True则该异常会被抑制
        # print("程序继续运行")  # 如果返回True则该异常会被抑制
except Exception as e:
    print(f"捕获到异常: {e}")
