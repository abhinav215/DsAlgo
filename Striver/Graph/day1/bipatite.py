from collections import deque

def isBipartite(self, graph):
    n = len(graph)
    color = [0]*n
      # print(color)
    for i in range(n):
        if color[i]==0:
            qu = deque([])
            qu.append([i,1])
            color[i]=1
            while len(qu)!=0:
                node,ithcolor = qu.popleft()
                for ele in graph[node]:
                    if color[ele]==ithcolor:
                        return False
                    if color[ele]==0:
                        qu.append([ele,-ithcolor])
                        color[ele] = -ithcolor
    return True




graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(isBipartite(graph))