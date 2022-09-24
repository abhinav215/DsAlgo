def solve(arr):
  n = len(arr)
  r = max(arr)
  for i in range(r):
    out = ""
    for j in range(n):
      if arr[j]>=r-i:
        out+="|"
      else:
        out+=" "
    print(out)

arr = [4,2,3,1,5]
solve(arr) 