# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def answer(arr,index,length,lt,ans):
  if index==length:
    ans.append(lt)
  original = arr[:]
  for i in range(index,length):
    arr[i],arr[index]=arr[index],arr[i]
    answer(arr,index+1,length,lt+[arr[index]],ans)
    arr=original[:]


def permute(arr):
  n = len(arr)
  ans =[]
  answer(arr,0,n,[],ans)
  print(ans)
  return ans


nums = [1,2,3]
permute(nums)