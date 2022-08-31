from collections import deque


def bfs(V,adj):
  vis = []
  for i in range(V):
    vis.append(0)
  ans = []
  front = 0
  qu = deque([])
  qu.append(front)
  vis[front]=1
  while len(qu)!=0:
    front = qu.popleft()
    ans.append(front)
    for ele in adj[front]:
      if vis[ele]==0:
        qu.append(ele)
        vis[ele]=1
  print(ans)



n = 5 
adj  =[[1, 2, 3], [], [4], [], []]
bfs(n,adj)