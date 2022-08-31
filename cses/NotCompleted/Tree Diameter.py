
from collections import defaultdict


def diameter(index,root,maxi,parent):
  # print(index,parent)
  summ = 0
  maxim = 0
  if len(root[index])>0:
    for ele in root[index]:
      if ele==parent:
        continue
      child = diameter(ele,root,maxi,index)
      summ += child
      maxim = max(maxim,child)
    maxi[0]= max(maxi[0],summ+1)
    return maxim+1
  return 1









def solve(n):
  adj = defaultdict(list)
  for i in range(n-1):
    txt = input()
    u,v = list(map(int,txt.split(" ")))
    adj[u].append(v)
    adj[v].append(u)
  # print(adj)
  ans =[0]
  diameter(1,adj,ans,-1)
  # print(diameter(1,adj,ans),"ans")
  # print("maxi=",ans)
  print(ans[0]-1)


n = int(input())
solve(n)