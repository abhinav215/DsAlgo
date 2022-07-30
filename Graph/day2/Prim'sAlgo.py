

import sys
#brute force tc = n^2

def answer(adj,n):
  key = [sys.maxsize]*n
  parent = [-1]*n
  mst = [False]*n

  key[0] = 0

  for i in range(n-1):
    mini = sys.maxsize
    node = -1
    for j in range(n):
      if key[j]<mini and mst[j]==False:
        mini = key[j]
        node = j

    mst[node]=True
      
    for ele in adj[node]:
      if mst[ele[0]]==False and ele[1]<key[ele[0]]:
        key[ele[0]] = ele[1]
        parent[ele[0]] = node
  print(parent)

  for ele in range(n):
    print(str(parent[ele])+">>>"+ str(ele))








adj = [[[1,2],[3,6]],[[0,2],[2,3],[3,8],[4,5]],[[1,3],[4,7]],[[0,6],[1,8]],[[1,5],[2,7]]]
answer(adj,5)