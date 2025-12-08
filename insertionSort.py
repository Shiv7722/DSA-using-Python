# Insertion sort, for each element looks backwords for its correct position and inserts it there by swaping other elements 
def selsort(l):
    n = len(l)
    if n<=1:
        return l
    
    for i in range(n):
        j=i
        while j>0 and l[j-1]>l[j]:
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
    return l

l=[4,43,56,17,12,1,14,23,19,34,5,7,5,9,14]
sorted=selsort(l)
print(sorted)