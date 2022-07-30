
def binarySearch(arr,num):
  start = 0
  end = len(arr)-1
  while start<=end:
    mid = (start+end)//2
    if arr[mid]<=num:
      start=mid+1
    else:
      end=mid-1
  return start



def smallerEqual(mid,arr):
  summ = 0
  for i in range(len(arr)):
    summ += binarySearch(arr[i],mid)
  return summ
  



def findMedian(arr):
  start = 0
  end = int(10e9)
  n= len(arr)
  m = len(arr[0])
  stopper= n*m//2
  while start<=end:
    # print(start,end)
    mid = (start+end)//2
    num = smallerEqual(mid,arr)
    if num>stopper:
      end = mid-1
    elif num <=stopper:
      start = mid+1
    print(start,end,num,stopper)
  print(start)
  return start




# A = [   [1, 3, 6],
#   [2, 6, 9],
#   [3, 6, 9]   ]

A=[   [1,2,3,3,6,6,6,9,9]  ]
#[1,2,3,3,6,6,6,9,9]

findMedian(A)