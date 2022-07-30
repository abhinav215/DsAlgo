def Matrix(r,c):
  ans = []
  for i in range(r):
    temp = [0]*c
    ans.append(temp)
  return ans

def Dfs(vis,grid,r,c,row,column):
  vis[r][c]=1
  # print(r,row,c,column,vis)
  # print(c,column ,"grid", grid[r][c+1] ,"vis" ,vis[r][c-1])
  if c+1<column and grid[r][c+1]=="1" and vis[r][c+1]==0:
    Dfs(vis,grid,r,c+1,row,column)
  if r<row-1 and grid[r+1][c]=="1" and vis[r+1][c]==0:
    Dfs(vis,grid,r+1,c,row,column)
  if c-1>=0 and grid[r][c-1]=="1" and vis[r][c-1]==0:
    Dfs(vis,grid,r,c-1,row,column)
  if r-1>=0 and grid[r-1][c]=="1" and vis[r-1][c]==0:
    Dfs(vis,grid,r-1,c,row,column)

def answer(grid):
  row = len(grid)
  column = len(grid[0])
  vis = Matrix(row,column)
  print(grid)
  print(vis)
  cnt=0
  for r in range(row):
    for c in range(column):
      if vis[r][c]==0 and grid[r][c]=="1":
        cnt+=1
        # print(cnt,r,c,"cnt",vis)
        Dfs(vis,grid,r,c,row,column)
        break
    break
  print(cnt)




grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid =[["1","1","1"],["0","1","0"],["1","1","1"]]
answer(grid)