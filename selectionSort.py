# Below is the naive approch to sort a python list
# this implementation occupies extra memory as it creates an extra list to store the 
# sorted list which is not required as we will see in the second implemetation

def sort(l):
    sorted=[]

    while len(l)>0:
        min=l[0]
        min_pos=0
        """below loop finds the minimum and the position 
        of the minimum among the (i+1)th to all the remaining element"""
        for j in range(1,len(l)):
            if l[j]< min:
                min=l[j]
                min_pos=j
        sorted.append(min)
        l.pop(min_pos)
    return sorted

# inplace selection sorting implemetation 
# as it selects the minimum element from the list and swaps it with the first element 
# and does the same for the second element, slects the minimum from remaining elements and swaps it with second element 
def insort(l):
    n = len(l)
    for i in range(n):
        min = l[i]
        minPos = i
        for j in range(i+1,n):
            if l[j]<min:
                min = l[j]
                minPos=j
        l[i],l[minPos]=min,l[i]
    return l    



L=[4,17,27,12,1,43,7,5,39,9,14,23,9,54]
insort(L)
print(L)