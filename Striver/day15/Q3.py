def romanToInt( s) -> int:
  dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  pre = 0
  ans = 0
  n=len(s)
  for i in range(n-1,-1,-1):
    # print(dic[s[i]])
    if pre<=dic[s[i]]:
      ans+=dic[s[i]]
    else:
      ans-=dic[s[i]]
    pre = dic[s[i]]
    print(ans,pre)
  print(ans,pre)
  return ans


s = "MCMXCIV"
romanToInt(s)