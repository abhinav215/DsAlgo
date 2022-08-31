
def answer(p1,p2):
  if p1>p2:
    return answer(p2,p1)
  if p1*2<p2 or (p1+p2)%3!=0:
    return "NO"
  return "YES"


t = int(input())
for test in range(t):
  txt = input()
  p1,p2 = list(map(int,txt.split(" ")))
  print(answer(p1,p2))