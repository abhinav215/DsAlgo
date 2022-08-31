from collections import deque
import sys

def answer(n,adj,src):
  distance=[sys.maxsize]*n
  qu = deque([])
  qu.append([src,0])
  distance[src]=0
  while len(qu)!=0:
    front,d = qu.popleft()
    for ele in adj[front]:
      if distance[ele]==sys.maxsize:
        qu.append([ele,d+1])
        distance[ele]=d+1
  print(distance)



adj = [[1,3],[0,2,3],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]]
src = 0
n=9
answer(n,adj,src)