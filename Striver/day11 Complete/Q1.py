# Nth root
import math




def findNthRootOfM(n,m):
  start=0
  end = math.ceil(m/2)
  print(start,end)
  if n==1:
    m ="{:.5f}".format(m)
    return m
  # i=0
  # while end-start>0.000001 and i<10:
  while end-start>0.000001:
    mid = (start+end)/2
    print(mid)
    npower = mid**n
    if npower ==m:
      ans = round(mid,5)
      ans ="{:.5f}".format(ans)
      return ans
    if npower>m:
      end = mid
    else:
      start = mid
    # i+=1
  ans = round(mid,5)
  ans ="{:.5f}".format(ans)
  print(ans)
  return mid



# n=3
# m=27


n=4
m= 69
findNthRootOfM(n,m)