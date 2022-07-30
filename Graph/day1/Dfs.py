from collections import deque

def dfs(node,adj,vis,ans):
  for ele in adj[node]:
    if vis[ele] == 0:
      ans.append(ele)
      vis[ele] = 1
      dfs(ele,adj,vis,ans)

def dfsOfGrapf(V,adj):
  vis = []
  for i in range(V):
    vis.append(0)
  ans = [0]
  vis[0] = 1
  node = 0
  dfs(node,adj,vis,ans)
  print(ans)
  return ans

n= 5 
adj  =[[1, 2, 3], [0], [0, 4], [0], [2], []]
dfsOfGrapf(n,adj)