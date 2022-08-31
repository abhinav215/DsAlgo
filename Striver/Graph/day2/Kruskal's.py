
def findParent(u,parent):
  if parent[u]==u:
    return u
  parent[u] = findParent(parent[u],parent)
  return parent[u]

def union(u,v,parent,rank):
  u =findParent(u,parent)
  v =findParent(v,parent)
  if rank[u]<rank[v]:
    parent[u] = v
  elif rank[u]>rank[v]:
    parent[v] = u
  else:
    parent[v] = u
    rank[u]+=1

def answer(n):
  parent = []
  for i in range(n):
    parent.append(i)
  rank= [0]*n
  
  edge = edgemaker()
  edge=sorted(edge, key = lambda x:x[2])
  print(edge)
  cost = 0
  for ele in edge:
    u,v,w = ele
    if findParent(u,parent)!=findParent(v,parent):
      union(u,v,parent,rank)
      cost += w
  print(cost)


def edgemaker():
  edge = []
  # (u,v,w)
  edge.append((0,1,2))
  edge.append((0,3,6))
  edge.append((1,0,2))
  edge.append((1,2,3))
  edge.append((1,3,8))
  edge.append((1,4,5))
  edge.append((2,1,3))
  edge.append((2,4,7))
  edge.append((3,0,6))
  edge.append((3,1,8))
  edge.append((4,1,5))
  edge.append((4,2,7))
  return edge


print(edgemaker())
print(answer(5))