from collections import deque

def edgeFormer(prerequisites,n):
  adj = []
  for i in range(n):
    adj.append([])
  for ele in prerequisites:
    if ele[1] not in adj[ele[0]]:
      adj[ele[0]].append(ele[1])
    if ele[0] not in adj[ele[1]]:
      adj[ele[1]].append(ele[0])
  return adj


def cycleBfs(node,adj,vis):
  qu = deque([])
  qu.append([node,-1])
  vis[node] = 1
  while len(qu)!=0:
    node,previous = qu.popleft()
    vis[node] = 1
    print(node,previous,vis)
    for ele in adj[node]:
      if vis[ele]==1 and ele!=previous:
        print(ele,vis,node)
        return True
      elif ele!=previous:
        qu.append([ele,node])
  return False 




def answer(numCourses,prerequisites):
  adj = edgeFormer(prerequisites,numCourses)
  print(adj)
  vis = []
  for i in range(numCourses):
    vis.append(0)
  for i in range(numCourses):
    if vis[i]==0:
      print("cycle")
      if cycleBfs(i,adj,vis):
        return True
  return False







numCourses = 8
prerequisites = [[0,2],[2,3],[1,4],[4,5],[6,7],[5,6],[7,4]]
# prerequisites = [[0,2],[2,3],[1,4],[4,5],[6,7],[5,6]]
print(answer(numCourses , prerequisites))
