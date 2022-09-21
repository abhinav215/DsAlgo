def solve(arr):
  n = len(arr)
  m = len(arr[0])
  for i in range(n):
    for j in range(1,m):
      arr[i][j] = arr[i][j]+arr[i][j-1]
  # print(arr)
  for j in range(m):
    for i in range(1,n):
      arr[i][j] = arr[i][j]+arr[i-1][j]
  # print(arr)
  for ele in arr:
    print(ele)

arr = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
solve(arr)