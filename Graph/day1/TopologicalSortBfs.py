from collections import deque

class Solution:
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # print(V,adj)
        indegree = [0]*V
        for ele in adj:
            for node in ele:
                indegree[node]+=1
        # print(indegree)
        qu = deque([])
        for i in range(V):
            if indegree[i]==0:
                qu.append(i)
        # print(qu)
        ans = []
        while len(qu)!=0:
            front = qu.popleft()
            ans.append(front)
            for ele in adj[front]:
                indegree[ele]-=1
                if indegree[ele]==0:
                    qu.append(ele)
        # print(ans)
        return ans