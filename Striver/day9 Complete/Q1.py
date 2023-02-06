

def answer(arr,summ,length,index,ans):
  if index==length:
    print(summ)
    ans.append(summ)
    return
  # print("index",index)
  answer(arr,summ+arr[index],length,index+1,ans)
  answer(arr,summ,length,index+1,ans)

def subsetSums(arr,n):
  ans = []
  answer(arr,0,n,0,ans)
  print(ans)
  ans = sorted(ans)
  print(ans)


N = 3
arr = [5, 2, 1]


subsetSums(arr,N)