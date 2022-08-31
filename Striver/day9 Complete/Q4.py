
def answer(arr,index,length,ans,lt,target):
  if target==0:
    ans.append(lt)
    return 
  if target<0:
    return 
  if index ==length:
    return 
  pre = None
  for i in range(index,length):
    if arr[i]!=pre:
      answer(arr,i+1,length,ans,lt+[arr[i]],target-arr[i])
      pre = arr[i]


def combinationSum2(nums,target):
  nums.sort()
  ans = []
  n= len(nums)
  answer(nums,0,n,ans,[],target)
  print(ans)
  return ans


candidates = [10,1,2,7,6,1,5] 
target = 8
combinationSum2(candidates,target)

# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]