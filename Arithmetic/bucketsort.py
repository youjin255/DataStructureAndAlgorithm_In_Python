from random import random
def insertsort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
    return A

def bucketsort(A):
    n=len(A)
    B=[]
    buckets=[[] for _ in range(len(A))]

    for a in A:
        buckets[int(a*n)].append(a)


    for i in buckets:
        B.extend(insertsort(i))
    return B
C=[]
for i in range(10):
    C.append(random())

D=bucketsort(C)
print(D)

