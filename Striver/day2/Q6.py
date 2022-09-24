
def merge(l,r,cnt):
  i = j = 0
  ans = []
  while i<len(l) and j<len(r):
    if l[i]<r[j]:
      ans.append(l[i])
      i+=1
    else:
      ans.append(r[j])
      j+=1
      cnt[0]+=len(l)-i
  ans = ans+l[i:]+r[j:]
  return ans

def solve(arr,cnt):
  n = len(arr)
  if n<2:
    return arr
  low = 0
  high = n-1
  mid = (low+high)//2
  # print(arr[:mid+1],arr[mid+1:])
  l = solve(arr[:mid+1],cnt)
  r = solve(arr[mid+1:],cnt)
  # print(l,r,arr)
  arr = merge(l,r,cnt)
  return arr


arr = [5,3,2,4,1]
cnt = [0]
print(solve(arr,cnt))
print(cnt[0])