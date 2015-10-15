def countsort(A,k):
    B=[0]*len(A)
    C=[0]*k
    for i in A:
        C[i]=C[i]+1
    for i in range(1,len(C)):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1

    return B
A=[2,3,5,1,9,6,8]
c=countsort(A,10)
print(c)



def countsort(A,k):
    C=[0]*k
    B=[0]*len(A)
    for i in A:
        C[i]=C[i]+1
    C[0]=C[0]-1

    for i in range(1,len(C)):
        C[i]=C[i]+C[i-1]

    for i in A:
        B[C[i]]=i
        C[i]=C[i]-1

    print(B)
A=[3,8,6,7,4,5,2,1,2]
countsort(A,9)