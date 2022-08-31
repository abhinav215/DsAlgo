class Node:
  def __init__(self,o,c,f) -> None:
    self.open = o
    self.close = c
    self.full = f

def merge(left,right):
  x= [0,0,0]
  x[2]=left[2]+right[2]+min( left[0], right[1])
  x[0]=left[0]+right[0]-min( left[0], right[1])
  x[1]=left[1]+right[1]-min( left[0], right[1])
  return x


def querry(index,low,high,l,r,seg):
  if low>=l and high<=r:
    return seg[index]
  if low>r or l>high:
    return [0,0,0]
  mid = (low+high)//2
  left = querry(2*index+1,low,mid,l,r,seg)
  right = querry(2*index+1,mid+1,high,l,r,seg)
  # print(left,right,mid)
  return merge(left,right)
  

def building(index,low,high,seg):
  if low==high:
    seg[index]=[0,0,0]
    if s[low]=="(":
      seg[index][0]+=1
    if s[low]==")":
      seg[index][1]+=1
    return
  mid = (low+high)//2
  building(index*2+1,low,mid,seg)
  building(index*2+2,mid+1,high,seg)
  seg[index]  = merge(seg[index*2+1],seg[index*2+2])
  


def answer(s,q):
  n = len(s)
  seg = [-1]*(4*n)
  building(0,0,n-1,seg)
  print(seg)
  for l,r in q:
    l = l-1
    r = r-1
    print(querry(0,0,n-1,l,r,seg)[2],"lol")

s = "())(())(())("
q=[[1,1],[2,3],[1,2],[1,12],[8,12],[5,11],[2,10]]
answer(s,q)