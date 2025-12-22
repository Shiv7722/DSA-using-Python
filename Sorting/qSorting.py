def qsort(L,l,r):
    if r-l<=1:
        return L
    
    pivot,lower,upper=L[l],l+1,l+1
    for i in range(l+1,r):
        if L[i]>pivot:
            upper+=1
        else:
            L[lower],L[i]=L[i],L[lower]
            lower+=1
            upper+=1
        
    L[lower-1],L[l]=L[l],L[lower-1]
    qsort(L,l,lower-1)
    qsort(L,lower,r)

L=[10,3,7,6,1,9,4,2,22,12,43,25,8]
qsort(L,0,len(L))
print(L)


    