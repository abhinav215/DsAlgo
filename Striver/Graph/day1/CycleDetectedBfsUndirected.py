from collections import deque


def EdgeAdder(graph,lt):
    graph[lt[0]].append(lt[1])



def topoSort(V, adj):
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
    cnt = 0
    while len(qu)!=0:
        front = qu.popleft()
        cnt+=1
        for ele in adj[front]:
            indegree[ele]-=1
            if indegree[ele]==0:
                qu.append(ele)
    print(cnt,V)
    if cnt == V:
        return True
    return False


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = []
        for i in range(numCourses):
            graph.append([])
        # print(graph)
        for ele in prerequisites:
            EdgeAdder(graph,ele)
        print(graph)
        return topoSort(numCourses,graph)
        