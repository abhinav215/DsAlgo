

# Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

# Input:
# txt = aabaabaa
# pat = aaba
# Output: 4
# Explanation: aaba is present 4 times
# in txt.

def answer(txt,pat):
  dic = {}
  for ele in pat:
    if ele not in dic:
      dic[ele]=0
    dic[ele]+=1
  print(dic)
  count = len(dic)
  n = len(txt)
  k=len(pat)
  ans = 0
  print(txt)
  for i in range(k-1):
    print(dic,txt[i])
    dic[txt[i]]-=1
    if dic[txt[i]]==0:
      count-=1
  print(dic,txt[:i+1],count,k)
  start  = 0
  print(i)
  end = i
  while end<n-1:
    end+=1
    dic[txt[end]]-=1
    if dic[txt[i]]==0:
      count-=1
    
    print(dic,txt[start:end+1],count)
    if count == 0:
      ans+=1
    if dic[txt[start]]==0:
      count+=1
    dic[txt[start]]+=1
    start+=1
  print(ans)









txt = "aabaabaa"
pat = "aaba"
answer(txt,pat)