
def setZeroes(self, matrix) -> None:
  r = len(matrix)
  c = len(matrix[0])
  row = [False]*r
  col = [False]*c
  for i in range(r):
    for j in range(c):
      if matrix[i][j]==0:
        row[i]=True
        col[j]=True 
  for i in range(r):
    for j in range(c):
      if row[i] or col[j]:
        matrix[i][j] = 0
  return matrix