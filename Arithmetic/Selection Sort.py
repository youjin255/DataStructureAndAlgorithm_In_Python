# Selection Sort 
import sys 
a = [ 170, 40, 72, 90, 802, 24, 2, 66, 32]

for i in range(len(a)): 
    min_idx = i 
    for j in range(i+1, len(a)): 
        if a[min_idx] > a[j]: 
            min_idx = j 
              
    a[i], a[min_idx] = a[min_idx], a[i] 

print ("Selection Sorted array: ") 
for i in range(len(a)): 
    print("%d \t" %a[i], sep=' ', end='', flush=True) 