def sortInRange(L,r):
    result = []
    li = {}
    for i in L:
            li[i] = li.get(i,0)+1

    uni = list(li.keys())
    for i in range(len(uni)):
        min=uni[i]
        minpos=i
        for j in range(i+1,len(uni)):
            if uni[j]<min:
                min=uni[j]
                minpos=j
              
        uni[i],uni[minpos]=uni[minpos],uni[i]
        result.extend([min]*li.get(min))
    
                
    return result

print(sortInRange([0,2,1,2,1,0,2,1,1,1,2,2,0,0,2,1,2,1,0,2,0,],2))