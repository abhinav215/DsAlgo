from collections import deque

def maxSlidingWindow(k,nums):
  n = len(nums)
  ans = []
  deq=deque([])
  for i in range(n):
    while len(deq)!=0 and nums[deq[-1]]<nums[i]:
      deq.pop()
    deq.append(i)
    if i>k-2:
      ans.append(nums[deq[0]])
    if deq[0]==i-k+1:
      print(deq)
      deq.popleft()
  print(ans)




nums = [1,3,-1,-3,5,3,6,7]
k= 3
maxSlidingWindow(k,nums)