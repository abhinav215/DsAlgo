


def kmp(s):
  n = len(s)
  ans = [0 for i in range(n)]
  # print(ans)
  i = 1
  j = 0
  while i<n:
    print(i,j)
    if s[i] == s[j]:
      ans[i] = j+1
      i+=1
      j+=1
    elif s[i] != s[j]:
      print(ans[j-1],j,"lol")
      j=ans[j-1]
      print(ans[j-1],j,"lol")
      if j==0:
        if s[0] == s[i]:
          ans[i] = j+1
          j+=1
        i+=1
  print(ans)



# s = "abcdabca"
s="aabaabaaa"
kmp(s)