import sys
sys.setrecursionlimit(20000)
L=["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77","a33"]

def merge(left,right):
    merged=[]
    i=j=0
    while i<len(left) and j<len(right):
        # here keep in mind to check for equality and insert the left element first in 
        # merged list to maintain the stability as the two similar element should be
        # in the same order as they are in the input list
        if ord(left[i][0])<=ord(right[j][0]):
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def mergeSort(L):
    if(len(L)<=1):
        return L
    
    mid=len(L)//2
    left=mergeSort(L[:mid])
    right=mergeSort(L[mid:])

    0.
    print(left,right)
    
    return merge(left,right)

sorted=mergeSort(L)
print(sorted)


