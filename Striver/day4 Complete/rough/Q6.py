# Length of Longest Substring without any Repeating Character



def answer(lt):
  print(lt,type(lt))
  n = len(lt)
  ans = 0
  count = 0
  lt2 =[]
  for i in range(n):
    print(ans)
    if lt[i] not in lt2:
      count+=1
      lt2.append(lt[i])
    else:
      ans = max(count,ans)
  print(ans)
  print(lt2)


s = "abcabcbb"
lt = list(s)
answer(lt)