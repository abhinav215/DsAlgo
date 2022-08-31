from collections import deque

def answer(nums):
  # print(nums)
  n = len(nums)
  dp = [-1]*3
  # print(n)
  if n<=2:
    return nums[n-1]
  dp[0] = nums[0]
  dp[1] = nums[1]
  dp[2] = nums[0]+nums[2]
  dp = deque(dp)
  for i in range(3,n):
    # print(dp)
    present = nums[i] + max(dp[0],dp[1])
    dp.popleft()
    dp.append(present)
  # print(dp)
  return dp[-1]


def houseRobber(valueInHouse):
  n = len(valueInHouse)
  b = answer(valueInHouse[:n-1])
  print(b,"b")
  a = answer(valueInHouse[1:])
  print(a,"a")
  return max(a,b)

print(houseRobber([1 ,5, 1 ,2, 6]))
print(houseRobber([2,3,5]))
print(houseRobber([1 ,3, 2, 0]))