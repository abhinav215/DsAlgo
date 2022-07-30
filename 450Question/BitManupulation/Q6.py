# Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.

# Example 1:

# Input:
# N = 2
# Output:
# 2


def findPosition(self, N):
  if N==0:
    return -1
  if N& N-1!=0:
    return -1
  cnt = 0 
  while N!=0:
    N = N>>1
    cnt +=1
  return cnt
    