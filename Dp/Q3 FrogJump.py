from typing import *
import sys

# memoziation
# def answer(index,height,dp):
#     if index==0:
#         return 0
#     if dp[index]!=-1:
#         return dp[index]
#     r = sys.maxsize
#     l = answer(index-1,height,dp) + abs(height[index]-height[index-1])
#     if index>1:
#         r = answer(index-2,height,dp) + abs(height[index]-height[index-2])
#     dp[index] =  min(r,l)
#     return dp[index]
  
# def frogJump(n: int, heights: List[int]) -> int:
#     dp = [-1]*n
#     return (answer(n-1,heights,dp))


# tabulation
# def frogJump(n,heights):
#   dp = [0]*(n+1)
#   dp[0] =0
#   dp[1] = abs(heights[1]-heights[0])
#   for i in range(2,n,1):
#     dp[i] = min(dp[i-1]+abs(heights[i]-heights[i-1]),dp[i-2]+abs(heights[i]-heights[i-2]))
#     print(i,dp[i],heights[i],heights[i-1],heights[i-2])
#   print(dp[n-1])



# spaceOptimization
def frogJump(n,heights):
  # dp = [0]*(n+1)
  pre2 =0
  pre = abs(heights[1]-heights[0])
  for i in range(2,n,1):
    curr = min(pre+abs(heights[i]-heights[i-1]),pre2+abs(heights[i]-heights[i-2]))
    pre2  = pre
    pre = curr
    # print(i,dp[i],heights[i],heights[i-1],heights[i-2])
  print(curr)

n = 43
heights = [17, 8, 16, 2, 8, 17, 9, 8, 15, 15, 5, 10, 8, 16, 11, 8 ,3, 2, 10, 18 ,5 ,5, 6 ,4 ,18, 1 ,11, 8, 18, 2, 13, 8 ,20 ,17 ,17 ,9 ,7 ,14, 9, 11, 7 ,18 ,17] 
frogJump(n,heights)
