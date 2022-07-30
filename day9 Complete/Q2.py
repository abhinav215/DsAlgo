
def answer(arr,lt,length,index,ans):
  if index > length:
    print(lt,index,"boom")
    return 
  ans.append(lt)
  pre = None
  print("start",lt)
  for i in range(index,length):
    if arr[i]!=pre:
      # print(arr[i])
      print(lt,index,i)
      answer(arr,lt+[arr[i]],length,i+1,ans)
      pre = arr[i]



def subsetsWithDup(numbs):
  ans = []
  n= len(numbs)
  answer(numbs,[],n,0,ans)
  print(ans)


# numbs = [1,2,2,2,3,3]
numbs = [1,2,2]
subsetsWithDup(numbs)