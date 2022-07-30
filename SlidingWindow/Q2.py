# arr = 2,2,4,5,1,1,1,1,2,3,3
# summ = 5
# find sub array with largest size having summ of element of sub array as summ


def answer(arr,summ):
  start = end = 0
  presentSumm = 0
  n = len(arr)
  maxlen = 0
  while end<n :
    if presentSumm == summ:
      maxlen = max(maxlen,end-start)
      presentSumm-=arr[start]
      presentSumm+=arr[end]
      end+=1
      start+=1
    elif presentSumm > summ:
      presentSumm-=arr[start]
      start+=1
    else:
      presentSumm+=arr[end]
      end+=1
    # print(presentSumm,n,end,start)
  print(maxlen)




arr=[2,2,4,5,1,1,1,1,2,3,3]
summ = 5
answer(arr,summ)