
def answer(grid,i,j1,j2,n,dp,dir):
#     print(i,j1,j2)
    if j1<0 or j1>=n or j2<0 or j2>=n:
        return -(10**8)
    if i == len(grid)-1:
        if j1==j2:
            return grid[i][j1]
        return grid[i][j1]+grid[i][j2]
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2] 
    maxi = 0
    for dj1 in dir:
        for dj2 in dir:
            ret = answer(grid,i+1,j1+dj1,j2+dj2,n,dp,dir)
            maxi = max(maxi,ret)
    if j1==j2:
        dp[i][j1][j2] = maxi + grid[i][j1]
        return dp[i][j1][j2] 
    dp[i][j1][j2] = maxi + grid[i][j1] + grid[i][j2]
    return dp[i][j1][j2] 
    

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    n = len(grid[0])
    dir = [-1,0,1]
    dp = []
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp2 =[-1]*len(grid[0])
            temp.append(temp2)
        dp.append(temp)
    return answer(grid,0,0,n-1,n,dp,dir)
