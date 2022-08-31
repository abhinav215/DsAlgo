
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

def cycleDfs(node,previous,adj,vis):
  vis[node] = 1
  # print(node,vis)
  for ele in adj[node]:
    print(ele,previous,vis)
    if ele!=previous and vis[ele]!=0:
      vis[ele]=1  
      # print(ele,previous,"False",vis)
      return False
    if ele!=previous:
      vis[ele]=1
      return cycleDfs(ele,node,adj,vis)
  return True
    

def answer(numCourses,prerequisites):
  adj = edgeFormer(prerequisites,numCourses)
  print(adj)
  vis = []
  for i in range(numCourses):
    vis.append(0)
  for i in range(numCourses):
    if vis[i]==0:
      print("lol",vis,i)
      ans = cycleDfs(i,-1,adj,vis)
      print(ans)
      if ans==False:
        return False
  return True



# numCourses = 2
# prerequisites = [[1,0],[0,1]]
# prerequisites = [[1,0]]



numCourses = 8
prerequisites = [[0,2],[2,3],[1,4],[4,5],[6,7],[5,6],[7,1]]
# prerequisites = [[0,2],[2,3],[1,4],[4,5],[6,7],[5,6]]
print(answer(numCourses , prerequisites))

