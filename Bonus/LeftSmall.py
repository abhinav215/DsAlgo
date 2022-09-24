# Count number of contiguous lesser elements to the left for each element in the given array.
import sys

def top(st):
  if len(st)==0:
    return -1
  else:
    return st[-1]

#stack of index with arr[index] decreasing
def solve(arr):
  n = len(arr)
  arr.append(sys.maxsize)
  st = []
  ans = []
  for i in range(n):
    cnt = 0
    while arr[i]>arr[top(st)]:
      st.pop()
      cnt+=1
    st.append(i)
    ans.append(cnt)    
  print(ans)


arr = [4,2,7,5,1,6]
print(solve(arr))
out = [0,0,2,0,0,2]