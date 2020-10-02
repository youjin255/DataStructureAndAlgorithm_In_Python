#shellSort
def shellSort(a): 
    n = len(a) 
    gap = n//2
    while gap > 0: 
  
        for i in range(gap,n): 
            temp = a[i] 
            j = i 
            while  j >= gap and a[j-gap] >temp: 
                a[j] = a[j-gap] 
                j -= gap 
            a[j] = temp 
        gap //= 2
  
a = [ 12, 34, 54, 2, 3] 
  
n = len(a) 
shellSort(a) 
print ("\nArray after sorting:") 
for i in range(n): 
    print("%d\t" %a[i], sep=' ', end='', flush=True)
  