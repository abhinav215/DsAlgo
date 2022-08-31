# Input
# 4
# 4
# Output
# 30
# Expected
# 20


def countPath(i,j,templt,n,m):
  print(i,j,n,m)
  if i==n-1 and j==m-1:
    return 1
  if i>=n or j>=m: 
    return 0
  if templt[i][j] != - 1: 
    return templt[i][j]
  templt[i][j] = countPath(i+1,j,templt,n,m)+countPath(i,j+1,templt,n,m)
  return templt[i][j]


def answer(n,m):
  templt=[]
  for i in range(n):
    column = []
    for j in range(m):
      column.append(-1)
    templt.append(column)
  print (countPath(0,0,templt,n,m))
  print(templt)


#n is row
#m in column
n=4
m=4
print(answer(n,m))