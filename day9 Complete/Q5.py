# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

def isPalindrome(st):
  n=len(st)
  start =0
  end = n-1
  while start<end:
    if st[start]==st[end]:
      start+=1
      end-=1
    else:
      return False
  return True


def answer(arr,index,length,ans,lt):
  if index ==length:
    ans.append(lt)
    return
  for i in range(index,length):
    if isPalindrome(arr[index:i+1]):
      answer(arr,i+1,length,ans,lt+[arr[index:i+1]])



def partition( s: str):
    ans = []
    n = len(s)
    answer(s,0,n,ans,[])
    # print(isPalindrome(s))
    print(ans)
    return ans


s = "aab"
partition(s)