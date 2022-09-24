# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


# better optimization

class Solution:
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


# most optimized


class Solution:
    def setZeroes(self, matrix) -> None:
      r = len(matrix)
      c = len(matrix[0])
      col0 = False
      for i in range(r):
        if matrix[i][0]==0:
            col0 = True
        for j in range(1,c):
          if matrix[i][j]==0:
            matrix[i][0] = matrix[0][j] = 0
      # print(matrix,"aaa")
      for i in range(r-1,-1,-1):
        for j in range(c-1,0,-1):
          if matrix[i][0]==0 or matrix[0][j]==0:
            matrix[i][j] = 0
        if col0==True:
          matrix[i][0]=0
      # print(matrix)
          