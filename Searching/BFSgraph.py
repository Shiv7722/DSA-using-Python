import sys
sys.path.append(r'F:\Code\DSA-using-Python\Data Structure')
# from LinkedList import LinkedList
from Queue2 import Queue2
import numpy as np

edges =  [(0,2), (1,2), (2,1), (1,3), (3,4),(2,3)]
mat = np.zeros(shape=(5,5))
for (i,j) in edges:
    mat[i,j]=1

print(mat)

def search(mat, v):
    (rows,cols)=mat.shape

    visited={}
    for i in range(rows):
        visited[i]=False
    
    q=Queue2()
    visited[v]=True
    q.enqueue(v)

    while q.head is not None:
        current=q.dequeue()
        for i in range(cols):
            if mat[current,i]==1 and (visited[i]==False):
                visited[i]=True
                q.enqueue(i)

    return visited

print(search(mat,2))
        
                
   
    

