# import sys
# sys.setrecursionlimit(10**7)

# def answer(i,j,grid,dp):
#     if i<0 or j<0:
#         return sys.maxsize
#     if i==0 and j==0:
#         return grid[0][0]
#     if dp[i][j] != -1:
#         return dp[i][j]
#     up = grid[i][j] + answer(i-1,j,grid,dp)
#     left = grid[i][j] + answer(i,j-1,grid,dp)
#     dp[i][j] = min(left,up)
#     return dp[i][j]


# def minSumPath(grid):
#     dp = []
#     for i in range(len(grid)):
#         temp = [-1]*(len(grid[0]))
#         dp.append(temp)
#     return answer(len(grid)-1,len(grid[0])-1,grid,dp)
   









# space optimization

import sys
sys.setrecursionlimit(10**7)

def answer(i,j,grid,dp):
    if i<0 or j<0:
        return sys.maxsize
    if i==0 and j==0:
        return grid[0][0]
    if dp[i][j] != -1:
        return dp[i][j]
    up = grid[i][j] + answer(i-1,j,grid,dp)
    left = grid[i][j] + answer(i,j-1,grid,dp)
    dp[i][j] = min(left,up)
    return dp[i][j]


def minSumPath(grid):
    dp = []
    for i in range(len(grid)):
        temp = [-1]*(len(grid[0]))
        dp.append(temp)
#     return answer(len(grid)-1,len(grid[0])-1,grid,dp)
    dp = [sys.maxsize]*len(grid[0])
    for i in range(len(grid)):
        temp = [0]*len(grid[0])
        for j in range(len(grid[0])):
            if i==0 and j==0:
                temp[j] = grid[0][0]
                continue
            elif j==0:
                temp[j] = grid[i][j] + dp[j]
                continue
            temp[j] = grid[i][j] + min(temp[j-1],dp[j])
        dp = temp[:]
#         print(dp)
    return dp[len(grid[0])-1]
   