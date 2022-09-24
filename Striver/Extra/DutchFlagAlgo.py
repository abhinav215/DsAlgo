def solve(arr):
  n = len(arr)
  low = 0
  high = n-1
  i = 0
  while high+1>=i:
    print(arr,low,high,i)
    # print(arr[i])
    if arr[i]==0:
      arr[i],arr[low] = arr[low],arr[i]
      low+=1
    if arr[i]==2:
      arr[i],arr[high] = arr[high],arr[i]
      high-=1
    else:
      i+=1

arr = [0,1,0,0,2,1,1,0,1,2]
arr = [0,1,0,0,0,1,1,1,2,0,1,2]
solve(arr)