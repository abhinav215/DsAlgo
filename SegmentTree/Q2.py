# MaxSum from l to r index
# arr = [8,2,5,1,4,5,3,9,6,10]
# l=3,r=8
# O/P =9

import sys

def building(index,low,high,seg,arr):
  # print(low,high)
  if low==high:
    # print(index,low)
    seg[index] = arr[low]
    return
  mid = (low+high)//2
  building(2*index+1,low,mid,seg,arr)
  building(2*index+2,mid+1,high,seg,arr)
  seg[index] = max(seg[index*2+1],seg[index*2+2])

def query(index,low,high,l,r,seg):
  # print(low,high,l,r)
  if low>=l and high<=r:
    return seg[index]
  if low>r or l>high:
    return -sys.maxsize
  mid = (low+high)//2
  a = query(2*index+1,low,mid,l,r,seg)
  b=query(2*index+2,mid+1,high,l,r,seg)
  # print(a,b)
  return max(a,b)

def update(index,i,val,low,high,seg):
  if low == high:
    seg[low] = val
    return
  mid = (low+high)//2
  if i<=mid:
    update(index,i,val,low,mid,seg)
  else:
    update(index,i,val,mid+1,high,seg)
  seg[index] = min(seg[index*2+1],seg[index*2+2])

def answer(arr):
  n = len(arr)
  seg = [0]*30
  building(0,0,n-1,seg,arr)
  print(seg)
  for i in range(1):
    l= int(input())
    r = int(input())
    print(query(0,0,n-1,l,r,seg))
  for i in range(1):
    i = int(input())
    val = int(input())
    update(0,i,val,0,n-1,seg)
  
  print(seg)

arr = [8,2,5,1,4,5,3,9,6,10]
answer(arr)