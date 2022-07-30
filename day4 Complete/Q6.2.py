#Length of Longest Substring without any Repeating Character

def answer(s):
  sett = []
  lt=list(s)
  print(lt)
  n = len(lt)
  print(n)
  if n==0:
    return 0
  if n==1:
    return 1
  r=l=0
  maxi =0
  count=0
  while r<n-1 or (lt[l]==lt[r] and l<n-1):
    print("emergency",n)
    if lt[r] not in sett:
      sett.append(lt[r])
      r+=1
      
    else:
      sett.pop(0)
      l+=1
      count = r-l+1
      if count>maxi:
        maxi=count
      count-=1
    print(count,lt[r],r,lt[l],l)
  # print(maxi)
  return (maxi)






s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s= "a"
# s= "au"
s=""
print(answer(s))