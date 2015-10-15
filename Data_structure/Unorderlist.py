class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getdata(self):
        return self.data

    def setdata(self,newdata):
        self.data=newdata

    def setnext(self,newdata):
        self.next=newdata

    def getnext(self):
        return self.next

class Unorderlist:
    def __init__(self):
        self.head=None

    def add(self,item):
        temp=Node(item)
        temp.setnext(self.head)
        self.head=temp

    def size(self):
        count=0
        current=self.head
        while current != None:
            count +=1
            current =current.getnext()

        return count

    def search(self,item):
        current=self.head
        found=False

        while current !=None and not found:
            if current.getdata()==item:
                found=True
            else:
                current=current.getnext()
        return found
    def remove(self,item):
        pre=None
        current = self.head
        found= False

        while not found:
            if current.getdata()==item:
                found=True
            else:
                pre=current
                current=current.getnext()

        if pre==None:
            self.head=current.getnext()

        else:
            pre.setnext(current.getnext())




A=Unorderlist()
A.add(1)
A.add(2)
A.add(3)
current=A.head
for i in range(A.size()):
    print(current.getdata())
    current=current.getnext()
