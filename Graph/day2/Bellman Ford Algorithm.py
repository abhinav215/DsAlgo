

import sys


def answer(edge,n,src):
  dist = [sys.maxsize]*n
  dist[src]=0
  for i in range(n-1):
    for ele in edge:
      print(edge)
      u,v,w = ele
      if dist[v]>dist[u]+w:
        dist[v]=dist[u]+w
  print(dist)







n=6
addEdge=[]
addEdge.append([3,2,6])
addEdge.append([5,3,1])
addEdge.append([0,1,5])
addEdge.append([1,5,-3])
addEdge.append([1,2,-2])
addEdge.append([3,4,-2])
addEdge.append([2,4,3])
src = 0
answer(addEdge,n,src)