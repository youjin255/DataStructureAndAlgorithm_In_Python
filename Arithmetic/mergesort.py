def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    B=[]
    C=[]
    for i in range(n1):
        B.append(A[p+i])
    for j  in range(n2):
        C.append(A[q+1+j])
    x=float("Inf")
    B.append(x)
    C.append(x)
    i=0
    j=0
    k=p

    while k<=r:
        if B[i]>C[j]:
            A[k]=C[j]
            k +=1
            j +=1
        else:
            A[k]=B[i]
            k +=1
            i +=1

def mergesort(A,p,r):
    if p<r:
        q=(p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

A=[1,2,9,8,7,4]
mergesort(A,0,5)
print(A)
