def mergesort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                mylist[k]=left[i]
                i = i+1
                k=k+1
            else:
                mylist[k]=right[j]
                k =k+1
                j=j+1
        if i<len(left):
            mylist[k]=left[i]
            k =k +1
            i=i+1
        else:
            mylist[k]=right[j]
            k=k+1
            j=j+1
   
