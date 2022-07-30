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


def countSetBits(n):
  msb = 1
  count =0
  while (msb<=n):
    msb=msb<<1
    count+=1
  print(count,"Most significant bit number")

  if count ==0:
    return 0

  x = count -1
  print(x)
  print((x)*(1<<(x-1)),n,"1 hai ye")
  print((n-(1<<x)+1),n,"2 hai ye")
  ans = (x)*(1<<(x-1)) + (n-(1<<x)+1) + countSetBits(n-(1<<x) )
  print(ans)
  return ans


# n=11
n=4
n=17
countSetBits(n)