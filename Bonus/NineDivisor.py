import math


def seive(arr):
    arr[0]= arr[1] = -1
    for i in range(math.ceil(math.sqrt(len(arr)))):
      if arr[i]==0:
        n = 2
        while i*n<len(arr):
          arr[i*n] += 1
          n+=1
        


# arr = [True]*(10^5+2)
arr = [0]*(200)
seive(arr)
print(arr)
for i in range(len(arr)):
  if arr[i]==0:
    # print(i)
    pass
print(arr[36])
print(arr[16])
print(arr[144])













# ==================================================================================================================
import math

#User function Template for python3
def seive(arr):
    arr[0]= arr[1] = -1
    for i in range(2,math.ceil(math.sqrt(len(arr)))):
        if arr[i]==0:
            n = 2
            while i*n<len(arr):
                arr[i*n] += 1
                n+=1
        if arr[i]!=0:
            n = 2
            while i*n<len(arr):
                arr[i*n] = -1
                n+=1
            
        


arr = [0]*(10**5+2)
seive(arr)

class Solution:
    def nineDivisors(self, N):
        cnt = 0
        b = math.ceil(math.sqrt(N))
        print(arr[0:50])
        
        i = 2
        while i<=b:
            if arr[i]==2:
                cnt+=1
            i+=1
        print(cnt)
            
        i=2
        while i**4<=b and arr[i]==0:
            # print(i,"iiiiiii")
            cnt+=1
            i+=1
        return cnt
        

