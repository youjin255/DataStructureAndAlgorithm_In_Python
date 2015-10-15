class BinHeap:
    def __init__(self):
        self.heap=[0]
        self.current_size=0

    def perc_up(self,i):
        while i//2>0:

            if self.heap[i]<self.heap[i//2]:
                temp=self.heap[i]
                self.heap[i]=self.heap[i//2]
                self.heap[i//2]=temp
            i=i//2

    def min_child(self,i):
        if 2*i+1>self.current_size:
            return 2*i
        else:
            if self.heap[2*i]<self.heap[2*i+1]:
                return 2*i
            else:
                return 2*i+1
    def perc_down(self,i):
        while 2*i<=self.current_size:
            mc=self.min_child(i)
            if self.heap[i]>self.heap[mc]:
                temp=self.heap[i]
                self.heap[i]=self.heap[mc]
                self.heap[mc]=temp
            i=mc
    def insert(self,item):
        self.heap.append(item)
        self.current_size=self.current_size+1
        print('f')
        self.perc_up(self.current_size)
        print('u')

    def build_heap(self,alist):
        i=len(alist)//2
        self.current_size=len(alist)
        self.heap=[0]+alist
        while i>0:
            self.perc_down(i)
            i=i-1
A=BinHeap()
mylist=[9,4,6,5,7,1,8]
A.build_heap(mylist)
A.insert(3)
print(A.heap)