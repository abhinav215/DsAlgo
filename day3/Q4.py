# Find the Majority Element that occurs more than N/3 times

# Input: N = 5, array[] = {1,2,2,3,2}

# Ouput: 2

# Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.



def answer(nums):
  ans = []
  n= len(nums)
  compair = n/3
  dic = {}
  for ele in nums:
    if ele not in dic:
      dic[ele]=1
    else:
      dic[ele]+=1
  for key in dic:
    if dic[key]>compair:
      ans.append(key)
  return ans


N = 3
nums = [1,2,2,3,2]
print(answer(nums))
          