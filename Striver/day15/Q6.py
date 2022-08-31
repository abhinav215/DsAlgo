import math


def repeatedStringMatch(self, a: str, b: str) -> int:
  print(a,b)
  if b in a:
      return 1
  Alen = len(a)
  Blen = len(b)
  print(math.ceil(Blen/Alen)+1)
  s = a*(math.ceil(Blen/Alen)+1)
  print(b,s)
  if b not in s:
      return -1
  print(a,b[Blen-Alen:],"wao")
  if a == b[:Alen] or a == b[Blen-Alen:]:
      return math.ceil(Blen/Alen)
  if b in a*math.ceil(Blen/Alen):
      return math.ceil(Blen/Alen)
  return math.ceil(Blen/Alen)+1


print(repeatedStringMatch("abccb","cbabccb"))

print(repeatedStringMatch("bb","bbbbbbb"))

print(repeatedStringMatch("abc","cabcabca"))

print(repeatedStringMatch("abcd","cdabcdab"))
print(repeatedStringMatch("aa","a"))