

def answer(s,start,index,lt,ans):
  # print(s)
  n= len(s)
  if index==n:
    if s[start:index+1] in lt:
      ans.append(s)
    return
  print(s[start:index+1])
  if s[start:index+1] in lt:
    # s.insert(index+1," ")
    # answer(s,start+2,index+2,lt,ans)
    # s.pop(index+1)
    
    answer(s[:index+1]+" "+s[index+1:],index+2,index+2,lt,ans)

  answer(s,start,index+1,lt,ans)
    



def wordBreak(s, dictionary):
  # s = list(s)
  lt = list(map(str,dictionary.split(" ")))
  ans = []
  answer(s,0,0,lt,ans)
  print((ans))



n =6
dictionary = "god is now no where here"
s = "godisnowherenowhere"
wordBreak(s, dictionary)