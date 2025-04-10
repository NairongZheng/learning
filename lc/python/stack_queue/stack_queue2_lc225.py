from collections import deque
class MyStack:
    """
        用两个队列实现一个栈
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int):
        self.queue1.append(x)

    def pop(self):
        if self.empty():
            return None
        for i in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.popleft()

    def top(self):
        ans = self.pop()
        self.queue1.append(ans)
        return ans
        
    def empty(self):
        if self.queue1 or self.queue2:
            return False
        else:
            return True

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()