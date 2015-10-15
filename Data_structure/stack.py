class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1

    def Full(self):
        return self.top==self.size-1

    def Empty(self):
        return self.top==-1

    def push(self,contend):
        if self.Full():
            print( "The stack is full")
        else:
            self.stack.append(contend)
            self.top +=1

    def pop(self):
        if self.Empty():
            print("The stack is Empty")
        else:
            temp=self.stack.pop()
            self.top -=1
            return temp