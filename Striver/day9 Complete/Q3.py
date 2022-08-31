def answer(arr,target,index,length,final,ans):
  if target == 0:
    ans.append(final)
    return
  if target<0:
    return
  if index==length:
    return
  answer(arr,target-arr[index],index,length,final+[arr[index]],ans)#taking
  answer(arr,target,index+1,length,final,ans)#not taKING


def combinationSum(arr,target):
  n = len(arr)
  ans =[]
  answer(arr,target,0,n,[],ans)
  print(ans)
  return ans


candidates = [2,3,6,7]
target = 7

combinationSum(candidates,target)