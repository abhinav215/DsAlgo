# Find the Majority Element that occurs more than N/2 times

# Input Format: N = 3, nums[] = {3,2,3}

# Result: 3

# Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 



def answer(nums):
  n= len(nums)
  compair = n/2
  dic = {}
  for ele in nums:
    if ele not in dic:
      dic[ele]=1
    else:
      dic[ele]+=1
  for key in dic:
    if dic[key]>compair:
      return key
  return -1


N = 3
nums = [3,2,3]
print(answer(nums))
          