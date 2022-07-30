# Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

# Input : 
# N = 8
# A[] = {12, -1, -7, 8, -15, 30, 16, 28}
# K = 3
# Output :
# -1 -1 -7 -15 -15 0 

from collections import deque

def answer(arr,k):
  negative = deque([])
  start = end = 0
  n = len(arr)
  ans =[]
  print(arr)
  while end<n:
    if end-start+1<k:
      if arr[end]<0:
        negative.append(arr[end])
      end+=1
    else:
      print(arr[start:end+1],negative,end,start)
      if arr[end]<0:
        negative.append(arr[end])
      end+=1
      if len(negative)==0:
        print(0)
        ans.append(0)
      else:
        print(negative[0])
        ans.append(negative[0])
      if len(negative)!=0 and negative[0] == arr[start]:
        negative.popleft()
      start+=1
  print(ans)
    




# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k=3


N = 5
arr = [-8, 2, 3, -6, 10]
k = 2

answer(arr,k)