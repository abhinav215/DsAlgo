def permutation(n):
  per = 1
  for i in range(1,n+1):
    per*=i
  return per

def listmaker(n):
  lt = []
  for i in range(1,n+1):
    lt.append(i)
  return lt

def answer(n,k,ans,per,lt):
  if n<=0:
    return ans
  per = per//n
  number  = lt[(k//per)]
  ans+=str(number)
  lt.remove(number)
  k = k % per
  n-=1
  return answer(n,k,ans,per,lt)



def getPermutation( n: int, k: int) -> str:
  lt = listmaker(n)
  per = permutation(n)
  final =answer(n,k-1,"",per,lt)
  print(final)
  return final
        

# Input: n = 4, k = 9
# Output: "2314"

n = 4
k = 9
getPermutation(n,k)
