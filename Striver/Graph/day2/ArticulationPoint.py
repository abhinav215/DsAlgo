def Dfs(node,parent,adj ,timer,vis,tim,low):
  vis[node]=1
  timer[0] += 1
  tim[node] = low[node] =timer[0]
  for ele in adj[node]:
    if ele == parent:
      continue
    if vis[ele]==0:
      Dfs(ele,node,adj ,timer,vis,tim,low)
      low[node] = min(low[node],low[ele])
      # print(ele,node,low,tim)
      if low[ele]>=tim[node] and parent!=-1:#important line
        print(str(node))
    else:
      low[node] = min(low[node],tim[ele])



def answer(adj,n):
  vis = [0]*n
  it = [0]*n
  low = [0]*n
  timer = [0]
  for i in range(n):
    if vis[i]==0:
      Dfs(i,-1,adj,timer,vis,it,low)


def addEdge(u,v,adj):
  adj[u].append(v)
  adj[v].append(u)


n=13
adj = []
for i in range(n):
  adj.append([])

addEdge(1,2,adj)
addEdge(1,4,adj)
addEdge(3,2,adj)
addEdge(3,4,adj)
addEdge(5,4,adj)
addEdge(5,6,adj)
addEdge(6,7,adj)
addEdge(8,7,adj)
addEdge(8,9,adj)
addEdge(6,9,adj)
addEdge(8,10,adj)
addEdge(11,10,adj)
addEdge(12,10,adj)
addEdge(12,11,adj)
answer(adj,n)