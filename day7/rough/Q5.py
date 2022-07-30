def removeDuplicates(self, nums):
  head = 0
  n = len(nums)
  if n<2:
    return n
  count = 1
  for i in range(1,n):
    if nums[i]!=nums[head]:
      head+=1
      count+=1
      nums[head]=nums[i]
  print(nums)
  return count
        