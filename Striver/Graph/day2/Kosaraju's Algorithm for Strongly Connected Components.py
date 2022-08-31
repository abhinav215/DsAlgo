

def TopologicalSort(node,adj,stack,vis):
  vis[node] = 1
  for ele in adj[node]:
    # print("C",ele,vis,stack)
    if vis[ele]==0:
      TopologicalSort(ele,adj,stack,vis)
  stack.append(node)


def TransposeGraph(adj,n):
  newAdj = []
  for i in range(n):
    newAdj.append([])
  for i in range(n):
    for ele in adj[i]:
      newAdj[ele].append(i)
  return (newAdj)

def Dfs(node,temp,adj,vis):
  vis[node] = 1
  temp.append(node)
  for ele in adj[node]:
    # print(ele,vis,node)
    if vis[ele]==0:
      Dfs(ele,temp,adj,vis)

def answer(adj,n):
  vis = [0]*n
  stack = []
  # print(adj)
  for i in range(n):
    if vis[i]==0:
      TopologicalSort(i,adj,stack,vis)
  # print(stack)
  adj = TransposeGraph(adj,n)
  # print(adj)
  ans = []
  vis = [0]*n
  for i in range(n):
    temp = []
    if vis[i]==0:
      Dfs(i,temp,adj,vis)
    if temp!=[]:
      print(temp)


def addEdge(u,v,adj):
  adj[u].append(v)



n=6
adj = []
for i in range(n):
  adj.append([])

addEdge(1,2,adj)
addEdge(3,1,adj)
addEdge(2,3,adj)
addEdge(2,4,adj)
addEdge(4,5,adj)
answer(adj,n)