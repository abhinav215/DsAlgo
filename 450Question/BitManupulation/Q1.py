# Given a positive integer N, print count of set bits in it. 

# Input:
# N = 6
# Output:
# 2
# Explanation:
# Binary representation is '110' 
# So the count of the set bit is 2.


def setBits( n):
  count = 0
  while n!=0:
      n = n &n-1
      count +=1
  return count