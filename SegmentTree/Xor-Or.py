#               O               or of child
#           O       O           xor of child      or xor alternative haui
#         O   O   O   O         or of child
#       O O  O O O O  O O       ALL N ELEMENT
# given N = 2**n


# Logic
# if n==odd => start with Or
# if n=even => start with xor


def building(index,low,high,seg,arr,orr):
  if low==high:
    seg[index] = arr[low]
    return
  mid = (low+high)//2
  building(2*index+1,low,mid,seg,arr,not orr)
  building(2*index+2,mid+1,high,seg,arr,not orr)
  if orr:
    seg[index] = seg[index*2+1] | seg[index*2+2]
  else:
    seg[index] = seg[index*2+1] ^ seg[index*2+2]



def update(index,i,val,low,high,seg,orr):
  if low == high:
    seg[low] = val
    return
  mid = (low+high)//2
  if i<=mid:
    update(index,i,val,low,mid,seg,not orr)
  else:
    update(index,i,val,mid+1,high,seg,not orr)
  if orr:
    seg[index] = seg[index*2+1] | seg[index*2+2]
  else:
    seg[index] = seg[index*2+1] ^ seg[index*2+2]


def answer(arr,n):
  N = 2**n
  seg = [0]*30
  if n%2==0:
    building(0,0,N-1,seg,arr,False)
  else:
    building(0,0,N-1,seg,arr,True)
  print(seg)
  for i in range(4):
    i = int(input())
    val = int(input())
    if n%2==0:
      update(0,i,val,0,N-1,seg,False)
    else:
      update(0,i,val,0,N-1,seg,True)
    print(seg)

arr = [1,6,3,5]
# arr = [1,2,3,4]
answer(arr,2)