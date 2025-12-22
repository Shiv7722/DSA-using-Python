import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10**5)
print(sys.getrecursionlimit())


def merge(l1,l2):
    i,j,l=0,0,[]
    m,n=len(l1),len(l2)
    while i<m and j<n:
        if l1[i]<l2[j]:
            l.append(l1[i])
            i+=1
        elif l1[i]==l2[j]:
            l.append(l1[i])
            l.append(l2[j])
            i+=1
            j+=1
        else:  
            l.append(l2[j])
            j+=1
    if i != m:
        l.extend(l1[m:])
    if j != n:
        l.extend(l2[j:])
    return l

def mSort(l):
    n = len(l)
    if n<=1:
        return l
    left=mSort(l[:n//2])
    right=mSort(l[n//2:])
    sorted = merge(left,right)
    return sorted

el=[15,38,3,23,1,8,18,5,12,34]
sorted = mSort(el)
print(sorted)


