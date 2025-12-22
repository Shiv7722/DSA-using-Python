def countsort(L,r):
    count=[0]*(r+1)

    for i in L:
        count[i]+=1

    # for i in range(1,r):
    #     count[i]+=count[i-1]
    index=0
    for i in range(r+1):
        for j in range(count[i]):
            L[index]=i
            index+=1
    
L=[0,2,1,2,1,0,2,1,1,1,2,2,0,0,2,1,2,1,0,2,0,4]
countsort(L,4)
print(L)

