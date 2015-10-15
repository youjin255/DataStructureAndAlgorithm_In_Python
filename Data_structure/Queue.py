class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.head=1
        self.tail=1

    def Empty(self):
        return self.head==self.tail
    def Full(self):
        return (self.tail+1)%(self.size)==self.head

    def inqueue(self,contend):
        if self.Full():
            print ("The queue is full")
        else:
            if self.tail==self.size:
                self.queue.append(contend)
                self.tail=1
            else:
                self.queue.append(contend)
                self.tail +=1
    def dequeue(self):
        if self.Empty():
            print("The queue is empty")
        else:
            if self.head==self.size:
                temp=self.queue.pop()
                self.head=1
                return temp
            else:
                temp=self.queue.pop()
                self.head +=1
                return temp













class Queue:
    def __init__(self,size):
        self.size=size
        self.head=1
        self.tail=1
        self.queue=[]

    def isEmpty(self):
        return self.head==self.tail

    def isFull(self):
        if self.tail>self.head:
            return self.tail-self.head==self.size-1
        else:
            return self.head-self.tail==1

    def enqueue(self,argv):
        if self.isFull():
            print ("The queue is full")
        else:
            if self.tail==self.size:
                self.queue.append(argv)
                self.tail=1
            else:
                self.queue.append(argv)
                self.tail= self.tail+1

    def dequeue(self):

        if self.isEmpty():
            print("The queue is empty")

        else:
            if self.head==self.size:
                temp=self.queue.pop(0)
                self.head=1
            else:
                temp=self.queue.pop(0)
                self.head +=1
        return temp
A=Queue(3)
A.enqueue(1)
A.enqueue(2)
A.enqueue(3)
print(A.queue)



print(A.dequeue())
print(A.queue)
A.dequeue()

A.enqueue(1)
A.enqueue(2)
A.enqueue(3)
print(A.dequeue())
print(A.dequeue())
print(A.isEmpty())
print(A.isFull())
