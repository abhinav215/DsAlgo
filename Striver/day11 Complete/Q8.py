def check(distance,arr,cows):
  cow=1
  pre = arr[0]
  for i in range(1,len(arr)):
    # print(arr[i],pre,distance,cow)
    if arr[i]-pre>=distance:
      cow+=1
      pre = arr[i]
  # print(cow,distance,cows,"cows")
  if cow>=cows:
    return True
  return False



def aggresiveCows(cows,arr):
  n = len(arr)
  arr.sort()
  print(arr)
  low=1
  high =  arr[n-1]-arr[0]
  # print(low,high)
  res= None
  while(low<=high):
    mid = (low+high)//2
    # print("boom",res)
    if check(mid,arr,cows):
      res = mid
      low = mid+1
    else:
      high = mid-1
  print(res)
  return res

# cows=3
# arr=[1,2,4,8,9]


cows=4
arr=[15 ,13, 11, 9 ,7 ,6]
aggresiveCows(cows,arr)