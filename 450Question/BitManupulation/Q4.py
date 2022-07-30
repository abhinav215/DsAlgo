
# You are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert A to B.

# Example 1:

# Input: A = 10, B = 20
# Output: 4


def countBitsFlip(self,a,b):
  Xor = a^b
  count =0
  while Xor!=0:
    count +=1
    Xor = Xor & Xor-1
  return count