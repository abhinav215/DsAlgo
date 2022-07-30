

def search(arr,target):
  n= len(arr)
  low=0
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if arr[mid]==target:
      print(mid)
      return mid
    if arr[mid]>=arr[low]:
      #left is sorted
      if target>=arr[low] and target<=arr[mid]:
        high = mid-1
      else:
        low = mid+1
    else:
      #right is sorted
      if target>=arr[mid] and target<=arr[high]:
        low = mid+1
      else:
        high = mid-1
  print(low,mid,high,"end")
  return -1



nums = [4,5,6,7,0,1,2]
target = 4
search(nums,target)