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


def countSetBits(self,n):
  #Ignoring 0 as all the bits are unset. 
  n += 1
  count = 0
  
  x = 2
  #Counting set bits from 1 to n.
  while x//2 < n:
    #Total count of pairs of 0s and 1s.
    quotient = n//x
    #quotient gives the complete count of pairs of 1s.
    #Multiplying it with the (current power of 2)/2 will give
    #the count of 1s in the current bit.
    count += quotient * x // 2
    
    remainder = n % x
    #If the count of pairs is odd then we add the remaining 1s 
    #which could not be grouped together. 
    if remainder > x//2:
      count += remainder - x//2
    
    x = x*2
  #returning count of set bits.
  return count