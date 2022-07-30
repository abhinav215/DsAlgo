# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1}, 
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}

# D,L,R,U

def answer(irow,icol,arr,temp,ans,st,n):
  if irow==n-1 and icol==n-1:
    ans.append(st)
  #down
  if irow != n-1:
    if arr[irow+1][icol]==1 and temp[irow+1][icol]==0:
      temp[irow+1][icol] = 1
      answer(irow+1,icol,arr,temp,ans,st+"D",n)
      temp[irow+1][icol] = 0
  # left
  if icol !=0:
    if arr[irow][icol-1]==1 and temp[irow][icol-1]==0:
      temp[irow][icol-1] = 1
      answer(irow,icol-1,arr,temp,ans,st+"L",n)
      temp[irow][icol-1] = 0
  # right
  if icol !=n-1:
    if arr[irow][icol+1]==1 and temp[irow][icol+1]==0:
      temp[irow][icol+1] = 1
      answer(irow,icol+1,arr,temp,ans,st+"R",n)
      temp[irow][icol+1] = 0
  #up
  if irow != 0:
    if arr[irow-1][icol]==1 and temp[irow-1][icol]==0:
      temp[irow-1][icol] = 1
      answer(irow-1,icol,arr,temp,ans,st+"U",n)
      temp[irow-1][icol] = 0

def listmaker(n):
  ans = []
  for i in range(n):
    temp = [0]*n
    ans.append(temp)
  return ans

def findPath(n,arr):
  if arr[0][0]==0:
    return []
  temp = listmaker(n)
  temp[0][0]=1
  ans = []
  answer(0,0,arr,temp,ans,"",n)
  print(ans)




# N = 4
# m= [[1, 0, 0, 0],
#   [1, 1, 0, 1], 
#   [1, 1, 0, 0],
#   [0, 1, 1, 1]]


N =2
m = [[1, 1],[ 1 ,1]]
findPath(N,m)