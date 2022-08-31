from unittest import makeSuite


# makeSate
# findPare
# union



def makeSet(n):
  parent = []
  for i in range(n):
    parent.append(i)
  rank = [0]*n
  return [parent,rank]


def findParent(u,parent):
  if parent[u]==u:
    return u
  parent[u] = findParent(parent[u],parent)
  return parent[u]

def union(u,v,parent,rank):
  u = findParent(u,parent)
  v = findParent(v,parent)
  if rank[u]>rank[v]:
    parent[v] = u
  if rank[u]<rank[v]:
    parent[u] = v
  else:
    parent[v] = u
    rank[u]+=1
  print(parent)


def answer():
  n=8
  parent,rank = makeSet(n)
  for i in range(6):
    txt = input()
    u,v = list(map(int,txt.split(" ")))
    union(u,v,parent,rank)
  if findParent(2,parent)!=findParent(3,parent):
    print("different Component")
  else:
    print("Same Component")
  print(findParent(2,parent),findParent(3,parent))




answer()

# 1 2
# 2 3
# 4 5
# 6 7
# 5 6
# 3 7