class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        """
            遍历链表
        """
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self, newdata):
        """
            在链表列表的开头插入
        """
        NewNode = Node(newdata)
        # update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self, newdata):
        """
            在链表列表的末尾插入
        """
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
    def Inbetween(self, middle_node, newdata):
        """
            在两个数据点之间插入
        """
        if middle_node is None:
            print('The mentioned node is absent')
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    
    def RemoveNode(self, Removekey):
        """
            从链表中删除项目
        """
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if HeadVal == None:
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None


list = SLinkedList()
# list.headval = Node('Mon')
# e2 = Node('Tue')
# e3 = Node('Wed')

# # link first node to second node
# list.headval.nextval = e2

# # link second node to third node
# e2.nextval = e3

# # list.AtBegining('Sun')
# # list.AtEnd('Thu')
# list.Inbetween(list.headval.nextval, 'Fri')
list.AtBegining('Mon')
list.AtBegining('Tue')
list.AtBegining('Wed')
list.AtBegining('Thu')
list.RemoveNode('Tue')
list.listprint()
pass
