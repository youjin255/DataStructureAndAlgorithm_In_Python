# Counting sort 
string = "ROHANSAHANA"

def countSort(string): 
    output = [0 for i in range(256)] 
    count = [0 for i in range(256)] 
    ans = ["" for _ in string] 
    for i in string: 
        count[ord(i)] += 1
  
    for i in range(256): 
        count[i] += count[i-1] 
  
    for i in range(len(string)): 
        output[count[ord(string[i])]-1] = string[i] 
        count[ord(string[i])] -= 1
  
    for i in range(len(string)): 
        ans[i] = output[i] 
    return ans  

b = countSort(string) 
print("Sorted character array using Counting sort is %s" %(" ".join(b)))
