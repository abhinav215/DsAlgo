def Dfs(node,vis,st,adj):
    vis[node]=1
    for ele in adj[node]:
        if vis[ele]==0:
            Dfs(ele,vis,st,adj)
    st.append(node)



def topoSort(self, V, adj):
    # Code here
    vis = [0]*V
    st = []
    for ele in range(V):
        if not(vis[ele]):
            Dfs(ele,vis,st,adj)
    st.reverse()
    # print(st)
    return st