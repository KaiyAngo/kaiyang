"""
linklist.py
功能：实现单链表的构建和功能操作
重点代码
"""

#创建节点类
class Node:
    """
    思路：将自定义的类视为节点的生成类，实力对象中包含数据部分和指向下一个节点的ｎｅｘｔ

    """
    def __init__(self, value, next=None):
        self.value = value  # 有用数据
        self.next = next  # 循环下一个节点关系

# node1 = Node(1)
# node2 = Node(node1)
# node3 = Node(node2)
#

class LinkList:
    """
    思路：单链表类，生成对象可以进行増删改查
    """
    def __init__(self):
        self.head=Node(None)


# l=LinkList()
# node=Node(1)
# l.head.next=node
#
# print(l.head.next.value)
    def init_list(self,list_):
        p= self.head
        for item in list_:
            p.next=Node(item)
            p=p.next
    def show(self):
        p=self.head.next
        while p is not Node:
            print(p.value)
            p=p.next

l=LinkList()
l.init_list([1,2,3,4,5])
l.show()






