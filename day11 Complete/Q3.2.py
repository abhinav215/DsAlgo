
def singleNonDuplicate(arr):
  n = len(arr)
  start=0
  end = n-2
  while start<=end:
    mid = (start+end)//2
    print(start,end,mid)
    #chech left
    if arr[mid]==arr[mid^1]:
      start = mid+1
    else:
      end=mid-1
  print(start,end,mid,"end")
  print(start)
  return end




nums = [1,1,2,3,3,4,4,8,8]

singleNonDuplicate(nums)

