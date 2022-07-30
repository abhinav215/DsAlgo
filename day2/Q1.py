# [[1,2,3],[4,5,6],[7,8,9]]

#input
# 1 2 3
# 4 5 6 
# 7 8 9


# Output (rotate by 90degree clockwise)
# 7 4 1 
# 8 5 2 
# 9 6 3



#Brute Force
def rotate(lt):
  n = len(lt)
  ans = []
  for i in range(n):
    row = []
    for j in range(n-1,-1,-1):
      row.append(lt[j][i])
      # print(j,i)
    ans.append(row)
  # print(ans)
  return ans


def reverseRow(row):
  n = len(row)
  for i in range(n//2):
    row[i],row[n-1-i]=row[n-1-i],row[i]
  return row

def transpose(lt,n):
  for i in range(n):
    for j in range(i):
      # print(i,j)
      lt[i][j],lt[j][i]=lt[j][i],lt[i][j]
  # print(lt)
  return lt

def rotate2(lt):
  n = len(lt)
  lt = transpose(lt,n)
  for i in range(n):
    lt[i] = reverseRow(lt[i])
  # print(lt)
  return lt


lt = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(lt))
print(rotate2(lt))