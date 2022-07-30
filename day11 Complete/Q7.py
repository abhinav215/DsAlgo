

def AllocatementIsPossible(barrier,arr,n,k):
  numberOfStudent = 1
  pages = 0
  for i in range(n):
    if arr[i]>barrier:
      return False
    if arr[i]+pages<=barrier:
      pages += arr[i]
    else:
      numberOfStudent +=1
      pages= arr[i]
  if numberOfStudent>k:
    return False
  return True



def books(arr,k):
  n = len(arr)
  if k>n:
      return -1
  low = min(arr)
  high = 0
  for i in range(n):
    high+=arr[i]
  
  if k==1:
      return high

  res = None
  while low<=high:
    prevlow = low
    prevhigh = high
    mid = (low+high)//2
    if AllocatementIsPossible(mid,arr,n,k):
      res = mid
      high = mid+1
    else:
      low = mid-1
    # i+=1
    if prevlow==low and prevhigh ==high:
      break
  print(res)
  return res 

A = [ 87, 3, 27, 29, 40, 12, 3, 69, 9, 57, 60, 33, 99 ]
B = 3
books(A,B)