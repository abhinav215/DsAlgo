
def answer(n):
  lt = ""
  lt += str(n)+" "
  while n!=1:
    if n%2==0:
      n = n//2
    else:
      n = n*3+1
    lt += str(n)+" "
  print(lt)


n = int(input())
answer(n)