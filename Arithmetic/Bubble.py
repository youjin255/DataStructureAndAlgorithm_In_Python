def bubble(A):
    for i in range(len(A)):

        for j in range(len(A)-1,i+1,-1):
            print(j)
            if A[j]<A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp
               
A=[1,4,5,3]
bubble(A)
print(A)