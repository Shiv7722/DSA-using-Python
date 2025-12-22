
def qsort(L, l, r):
    if r-l<=1:
        return L
    
    pivot,lower,upper=L[l],l+1,l+1
    for i in range(l+1,r):
        if L[i]<pivot:
            L[lower],L[i]=L[i],L[lower]
            lower+=1
            upper+=1
        else:
            upper+=1
    L[lower-1],L[l]=L[l],L[lower-1]
    lower-=1
    qsort(L,l,lower)
    qsort(L,lower+1,r)
    

L=[3,7,5,43,3,88,9,1,2,9]
qsort(L,0,len(L)-1)
print(L)


    

