# Directed Acyclic Path

import sys


def Dfs(node,adj,st,vis):
  vis[node]=1
  for ele in adj[node]:
    print(ele)
    if vis[ele[0]]==0:
      Dfs(ele[0],adj,st,vis)
  st.append(node)


def Topological(adj,n):
  vis = [0]*n
  st = []
  for i in range(n):
    if vis[i]==0:
      Dfs(i,adj,st,vis)
  return st

def answer(adj,n):
  st = Topological(adj,n)
  print(st)
  distance = [sys.maxsize]*n
  node = st[-1]
  distance[node]= 0
  while len(st)!=0:
    node = st.pop()
    if distance[node]!=sys.maxsize:
      for ele in adj[node]:
        distance[ele[0]] = min(distance[ele[0]],distance[node]+ele[1])
  print(distance)

adj = [[[1,2],[4,1]],[[2,3]],[[3,6]],[],[[2,2],[5,4]],[[3,1]]]
n = 6
answer(adj,n)