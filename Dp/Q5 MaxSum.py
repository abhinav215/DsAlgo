
import sys

# def answer(index,dp,nums):
#   if index == 0:
#     dp[0] = nums[0]
#     return nums[0]
#   if index == 1:
#     dp[1] = nums[1]
#     return nums[1]
#   if dp[index]!=-1:
#     return dp[index]

#   maxi = -sys.maxsize
#   for i in range(2,index+1):
#     # print(nums[index],index,i)
#     maxi = max(maxi,nums[index] + answer(index-i,dp,nums))
#   dp[index] = maxi
#   return dp[index]




# def maximumNonAdjacentSum(nums):
#   n = len(nums)
#   dp = [-1]*n
#   answer(n-1,dp,nums)
#   print(dp)

# nums = [2 ,1, 4 ,9,7,12]
# maximumNonAdjacentSum(nums)











# def maximumNonAdjacentSum(nums):
#   print(nums)
#   n = len(nums)
#   dp = [-1]*n
#   dp[0] = nums[0]
#   dp[1] = nums[1]
#   for i in range(2,n):
#     print(i,nums[i],nums[i-2],nums[i-3])
#     if i-3<0:
#       dp[i] = nums[i] + dp[i-2]
#     else:
#       dp[i] = nums[i] + max(dp[i-2],dp[i-3])
#     print(dp)
#   print(dp)


# nums = [2 ,1, 4 ,9,7,12]
# maximumNonAdjacentSum(nums)




















from collections import deque


def maximumNonAdjacentSum(nums):
  print(nums)
  n = len(nums)
  dp = [-1]*3
  dp[0] = nums[0]
  dp[1] = nums[1]
  dp[2] = nums[0]+nums[2]
  dp = deque(dp)
  for i in range(3,n):
    print(dp)
    present = nums[i] + max(dp[0],dp[1])
    dp.popleft()
    dp.append(present)
  print(dp)


nums = [2 ,1, 4 ,9,7,12]
maximumNonAdjacentSum(nums)