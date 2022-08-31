
def answer(n):
  s1 = ""
  s2 = ""
  summ1 = summ2 =0
  n1 = n2 = 0
  while n!=0:
    if summ1<summ2:
      summ1+=n
      n1+=1
      s1+= str(n)+" "
    else:
      summ2+=n
      n2+=1
      s2+= str(n) + " "
    # print(summ1,summ2,n)
    n-=1
  # print(summ1,summ2)
  if summ1==summ2:
    print("YES")
    print(n1)
    print(s1)
    print(n2)
    print(s2)
  else:
    print("NO")




n = int(input())
answer(n)