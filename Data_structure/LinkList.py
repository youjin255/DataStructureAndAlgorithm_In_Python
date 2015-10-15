class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.pre=None
        self.next=None

    def setdata(self,newData):
        self.data=newData

    def getdata(self):
        return self.data

    def setnext(self,newVal):
        self.next=newVal

    def getnext(self,newval):
        return self.next

    def setpre(self,newVal):
        self.pre=newVal

    def getpre(self):
        return self.pre

class LinkedList:
    def __init__(self):
        self.head=Node(None)

    def add(self,item):
        t=Node(item)
        t.next=self.head
        self.head.pre=t
        self.head=t

    def size(self):
        t=self.head
        size=0
        while t.data !=None:
            size +=1
            t=t.next

        return size

    def ListSearch(self,k):
        x=self.head
        while x.data != k and x.data !=None:
            x=x.next
        return x

    def ListInsert(self,x):
        t=Node(x)
        t.next=self.head
        self.head.pre=t
        self.head=t

    def ListDelete(self,x):
        temp_node=self.ListSearch(x)
        temp_node.pre.next=temp_node.next
        temp_node.next.pre=temp_node.pre




A=LinkedList()

A.add(4)

A.add(3)
A.add(2)
A.add(1)
A.ListInsert(9)
A.ListDelete(2)

print(A.size())


