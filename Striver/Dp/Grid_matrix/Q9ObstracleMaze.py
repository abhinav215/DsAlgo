modu = 10**9+7

def mazeObstacles(n, m, mat):
    pre = [0]*m
    for i in range(n):
        temp=[0]*m
        for j in range(m):
#             print(i,j)
            if mat[i][j]==-1:         # ye extra add karo Q8
                temp[j] = 0             # walai part mai
                continue                  #
            if i==0 and j==0:
                temp[j] = 1
                continue
            if j==0:
                temp[j] = pre[j]
                continue
            temp[j] = pre[j] + temp[j-1]
#         print(temp)
        pre = temp[:]
    return temp[m-1]
