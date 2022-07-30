import sys
from queue import PriorityQueue


def answer(node,n):
  key = [sys.maxsize]*n
  parent = [-1]*n
  mst = [False]*n

  key[0] = 0
  qu = PriorityQueue()
  qu.put((0,0))

  for i in range(n-1):
    node = qu.get()[1]
    mst[node]=True

    for ele in adj[node]:
      weight = ele[1]
      element = ele[0]
      if mst[element]==False and key[element]>weight:
        key[element] = weight
        parent[element] = node
        qu.put((weight,element))

  print(parent)
  print(key)







adj = [[[1,2],[3,6]],[[0,2],[2,3],[3,8],[4,5]],[[1,3],[4,7]],[[0,6],[1,8]],[[1,5],[2,7]]]
answer(adj,5)