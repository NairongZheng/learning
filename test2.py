#构建双向链表
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
         
class Solution:
    def __init__(self):
        #双向链表头尾
        self.size = 0
        self.head = None
        self.tail = None
        #哈希表记录key值
        self.mp = dict()
     
    #将节点插入表头函数
    def insertFirst(self, node: Node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
     
    #移到表头函数
    def moveToHead(self, node: Node):
        #已经到了表头
        if node.pre == self.head: 
            return
        #将节点断开，取出来
        node.pre.next = node.next
        node.next.pre = node.pre
        #插入第一个前面
        self.insertFirst(node)
     
    #删去表尾函数，最近最少使用
    def removeLast(self):
        #哈希表去掉key
        self.mp.pop(self.tail.pre.key)
        #断连该节点
        self.tail.pre.pre.next = self.tail;
        self.tail.pre = self.tail.pre.pre
     
    #插入函数
    def set(self, key: int, val: int):
        #没有见过这个key，新值加入
        if key not in self.mp:
            node = Node(key, val)
            self.mp[key] = node
            #超出大小，移除最后一个
            if self.size <= 0:
                self.removeLast()
            #大小还有剩余
            else:
                #大小减1
                self.size -= 1
            #加到链表头
            self.insertFirst(node);
        #哈希表中已经有了，即链表里也已经有了
        else:
            self.mp[key].val = val
            #访问过后，移到表头
            self.moveToHead(self.mp[key])
     
    #获取数据函数
    def get(self, key: int) -> int:
        #找不到返回-1
        res = -1
        #哈希表中找到
        if key in self.mp:
            #获取
            res = self.mp[key].val
            #访问过后移到表头
            self.moveToHead(self.mp[key])
        return res
 
    def LRU(self , operators: List[List[int]], k: int) -> List[int]:
        res = []
        #构建初始化连接
        #链表剩余大小
        self.size = k
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        #遍历所有操作
        for i in range(len(operators)):
            op = operators[i]
            if op[0] == 1:
                #set操作
                self.set(op[1], op[2])
            else:
                #get操作
                res.append(self.get(op[1]))
        return res