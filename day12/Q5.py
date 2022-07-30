


def AllPossibleStrings(st):
  n=len(st)
  ans =[]
  for num in range(1,(1<<n)):
    subseq = ""
    for i in range(0,n):
      if (num & (1<<i)!=0):
        subseq += st[i]
    print(subseq,num)
    ans.append(subseq)
  ans.sort()
  print(ans)
  return ans


st="a"
AllPossibleStrings(st)