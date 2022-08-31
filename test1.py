
# step1:构建一个双向链表的类，记录key值与val值，同时一前一后两个指针。
# 用哈希表存储key值和链表节点，这样我们可以根据key值在哈希表中直接锁定链表节点，从而实现在链表中直接访问，能够做到O(1)时间访问链表任意节点。
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class Solution:

    def __init__(self, capacity: int):
        # write code here
        # step 2：记录双向链表的头、尾及LRU剩余的大小.（这个头尾就是像虚拟节点）
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.map = dict()
    
    def insertFirst(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
    
    def moveToHead(self, node):
        if node.pre == self.head:        # 已经到了表头
            return
        
        # 将节点断开，取出来
        node.pre.next = node.next
        node.next.pre = node.pre
        
        # 插入到第一个前面
        self.insertFirst(node)
    
    def removeList(self):
        self.map.pop(self.tail.pre.key)    # 哈希表去掉key
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre

    def get(self, key: int) -> int:
        # write code here
        result = -1        # 找不到返回-1
        if key in self.map:
            result = self.map[key].val
            self.moveToHead(self.map[key])        # 访问后移动到表头
        return result

    def set(self, key: int, value: int) -> None:
        # write code here
        if key not in self.map:    # 没有见过这个key，新值加入
            node = Node(key, value)
            self.map[key] = node
            if self.size <= 0:    # 超出大小，移除最后一个
                self.removeList()
            else:                # 大小还有剩余
                self.size -= 1    # 大小减一
            self.insertFirst(node)    # 加到链表头
        else:                        # 哈希表中已经有了，即链表里也已经有了
            self.map[key].val = value
            self.moveToHead(self.map[key])
    
#     def LRU(self, operations):
#         result = []
#         self.size = k
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.pre = self.head
#         for i in range

# Your Solution object will be instantiated and called as such:
# solution = Solution(capacity)
# output = solution.get(key)
# solution.set(key,value)