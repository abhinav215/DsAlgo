
# Given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. Find the other two numbers.


# Example 1:

# Input: 
# N = 2
# arr[] = {1, 2, 3, 2, 1, 4}
# Output:
# 3 4 
# Explanation:
# 3 and 4 occur exactly once.


def singleNumber( nums):
  Xor = 0
  n = len(nums)
  for ele in nums:
    Xor = Xor^ele
  print(Xor)
  #ele = 7
  #find least significant set bit
  number =1
  bit = 0
  while number & Xor == 0:
    number = number<<1
    bit+=1
  #bit = 0
  print(bit)

  withSetBit = 0
  withUnSetBit = 0

  for ele in nums:
    if ele & (1<<bit) != 0:
      withSetBit = withSetBit^ ele
    else:
      withUnSetBit = withUnSetBit ^ ele

  print(withSetBit,withUnSetBit)  
  if withUnSetBit<withSetBit:
    return (withUnSetBit,withSetBit)
  return (withSetBit,withUnSetBit)


nums = [19, 20, 7, 3 ,5 ,26 ,19 ,27, 20, 27, 3 ,16, 7, 5, 9, 25, 8, 9, 8, 26]
singleNumber(nums)