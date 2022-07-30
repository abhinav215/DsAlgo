# Count total set bits 
# This problem is part of GFG SDE Sheet. Click here to view more.   
# You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).


# Input: N = 4
# Output: 5
# Explanation:
# For numbers from 1 to 4.
# For 1: 0 0 1 = 1 set bits
# For 2: 0 1 0 = 1 set bits
# For 3: 0 1 1 = 2 set bits
# For 4: 1 0 0 = 1 set bits
# Therefore, the total set bits is 5.

def largestPowerOfTwo(n):
  x= 0
  while (1<<x)<=n:
    x+=1
  return x-1


def countSetBits2(n):
  # n 2 ki power hai
  x= largestPowerOfTwo(n)
  print(x)
  if x<=0:
    return 0
  return (x)*(1<<(x-1))+1


def countSetBits(n):
  # n 2 ki power nahi hai hai
  # 2 ki power jo n sai barabar hai ya choti hai
  x= largestPowerOfTwo(n)
  
  if x<=0:
    return 1

  ans = (x)*(1<<(x-1)) + (n-(1<<x)+1) + countSetBits(n-(1<<x))
  # print(ans,"ans",n)
  return ans


def answer(n):
  if n & n-1==0:
    return countSetBits2(n)
  return countSetBits(n)
  
# n=4
# n=17
n=11
n=30 #75
print(answer(n),"ans")