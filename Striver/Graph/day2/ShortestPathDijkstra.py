from queue import PriorityQueue
import sys


def answer(adj,n,src):
  qu = PriorityQueue()
  dis = [sys.maxsize]*n
  qu.put((0,src))
  dis[src] = 0
  # print(qu.empty())
  while not qu.empty():
    distance,node = qu.get()
    print(distance,node)
    for ele in adj[node]:
      # print(distance,ele[1],dis[ele[0]])
      if distance + ele[1]<dis[ele[0]]:
        dis[ele[0]] = distance + ele[1]
        qu.put((dis[ele[0]],ele[0]))
  print(dis)



adj = [[],[[2,2],[4,1]],[[1,2],[5,5],[3,4]],[[2,4],[4,3],[5,1]],[[1,1],[3,3]],[[2,5],[3,1]]]
n = 6
src = 1
answer(adj,n,src)