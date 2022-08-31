from collections import deque

def orangesRotting(grid):
  qu = deque([])
  row = len(grid)
  column = len(grid[0])
  total = 0
  rotten = 0
  for i in range(row):
    for j in range(column):
      if grid[i][j]==1:
        total+=1
      if grid[i][j]==2:
        qu.append([i,j,0])
        total+=1
        rotten+=1
  print(qu,total,"stat")
  if rotten == 0:
    if total ==0:
      return 0
    return -1
  count =rotten
  while len(qu)!=0:
    front = qu[0]
    i = front[0]
    j = front[1]
    minute = front[2]
    if i!=0 and grid[i-1][j]==1:#up
      qu.append([i-1,j,minute+1])
      grid[i-1][j] = 2
      count+=1
    if i!=row-1 and grid[i+1][j]==1:#down
      qu.append([i+1,j,minute+1])
      # print("down")
      grid[i+1][j] = 2
      count+=1
    if j!=0 and grid[i][j-1]==1:#left
      qu.append([i,j-1,minute+1])
      grid[i][j-1] = 2
      count+=1
    if j!=column-1 and grid[i][j+1]==1:#left
      qu.append([i,j+1,minute+1])
      grid[i][j+1] = 2
      count+=1
    #remove this ele
    qu.popleft()
    print(qu,count)
    # print(grid)
  print(qu,"end",count,total)
  if count== total:
    print("boom",minute)
    return minute
  print(-1)
  return -1





# num = [[2,1,1],[1,1,0],[0,1,1]]
# num = [[2,1,1],[0,1,1],[1,0,1]]
num = [[2,1,1],[1,1,1],[1,1,2]]
orangesRotting(num)