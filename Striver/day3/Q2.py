# Implement Pow(x,n)
import decimal


def answer(base,power):
  result =1
  while power!=0:
    if power%2==0:
      power = power//2
      base = base*base
    else:
      power-=1
      result = base*result
    print(power,base,result)
  print(result)
  print( decimal.Decimal(result).normalize())
  


x = 2.00000
n = 10
x = 2.10000
n = 3
answer(x,n)