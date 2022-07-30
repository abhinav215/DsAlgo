
def numberOfNOtes(value):
  lt =[1000, 500, 100, 50, 20, 10, 5, 2, 1]
  count = 0
  n = 9
  for i in range(n):
    a = value//lt[i]
    count+=a
    value  = value - a*lt[i]
    print(count,value,lt[i])
    if value==0:
      break
  print(count)



# V = 80
n = int(input())
for i in range(n):
  V = int(input())
  numberOfNOtes(V)