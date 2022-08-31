
def findMaxConsecutiveOnes(nums):
  count = 0 
  maxi = 0
  for ele in nums:
    if ele==1:
      count+=1
      maxi = max(maxi,count)
    else:
      count=0
  return maxi