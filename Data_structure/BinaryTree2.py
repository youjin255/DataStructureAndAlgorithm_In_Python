class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.left=None
        self.right=None

    def insertLeft(self,newNode):
        if self.left==None:
            self.left=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.left=self.left
            self.left=t
    def insertRight(self,newNode):
        if self.right==None:
            self.right=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.right=self.right
            self.right=t

    def getRootVal(self):
        return self.key
    def setRootVal(self,newVal):
        self.key=newVal
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
