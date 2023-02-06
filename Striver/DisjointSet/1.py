
def solve(edges,n):
  parent =[]
  for i in range(n):
    parent.append(i)
  rank = [0]*n

  def find(u):
    if parent[u]==u:
      return u
    return parent[parent[u]]

  def union(u,v):
    uPrnt = find(u)
    vPrnt = find(v)
    if rank[uPrnt] > rank[vPrnt]:
      parent[vPrnt]=uPrnt
      uPrnt+=1
    else:
      parent[uPrnt]=vPrnt
      vPrnt+=1
    
  for u,v in edges:
    union(u,v)
  print(parent)


edges = [[1,2],[2,3],[4,5],[5,6],[6,4],[7,5]]
n = 8
solve(edges,n)