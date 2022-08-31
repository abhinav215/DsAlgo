
def answer(n):
  if n==1:
    print("1")
    return "1"
  if n==2 or n==3:
    print("NO SOLUTION")
    return "NO SOLUTION"
  lt = ""
  num=0
  for i in range(n):
    num+=2
    if num>n:
      num=1
    lt+=str(num)+" "
  print(lt)


n = int(input())
answer(n)