
def threeSum(self, nums):
  triplet = []
  nums.sort()
  n = len(nums)
    # print(nums)
  for i in range(n):
    left = i+1
    right =n-1
    while left<right:
      summ = nums[i]+ nums[left] +nums[right]
      if summ==0:
        # print("gotcha",nums[i],nums[left] ,nums[right])
        lt = [nums[i],nums[left] ,nums[right]]
        if lt not in triplet:
          triplet.append(lt)
        right-=1
        left+=1
      elif summ>0:
        right-=1
      elif summ<0:
        left+=1
  return triplet

