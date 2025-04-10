class MyQueue:
    """
        用两个栈实现一个队列
        自己画图看看流程就知道了
    """
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int):
        """
            将元素 x 推到队列的末尾
        """
        self.stack1.append(x)

    def pop(self):
        """
            从队列的开头移除并返回元素
        """
        if self.empty():        # 如果队列是空的，没有元素，就返回None
            return None
        if self.stack2 == []:   # 如果栈2是空的，就先把栈1的都加过来，再操作
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
            返回队列开头的元素
        """
        ans = self.pop()
        self.stack2.append(ans)
        return ans

    def empty(self):
        """
            如果队列为空，返回 true ；否则，返回 false
        """
        if self.stack1 or self.stack2:
            return False
        else:
            return True


obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()
pass