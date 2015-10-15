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

    def insert(self,k):
        self.heap.append(k)
        self.current_size=self.current_size+1
        self.perc_up(self.current_size)

    def min_child(self,i):
        if i*2+1>self.current_size:
            return i*2
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

    def build_heap(self,alist):
        self.current_size=len(alist)
        i=len(alist)//2
        self.heap=[0]+alist
        while(i>0):
            self.perc_down(i)
            i=i-1

    def HeapSort(self,alist):
        self.build_heap(alist)
        while self.current_size>=2:
            temp=self.heap[1]
            self.heap[1]=self.heap[self.current_size]
            self.heap[self.current_size]=temp
            self.current_size=self.current_size-1
            self.perc_down(1)




A=BinHeap()
mylist=[3,4,5,2,7,9,8]
A.HeapSort(mylist)
print(A.heap)





