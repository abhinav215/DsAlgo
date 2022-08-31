# Input
# 4
# 4
# Output
# 30
# Expected
# 20




def answer(n,m):
  total = n+m-2
  summ =1
  for i in range(n-1):
    summ *= (total-i)/(i+1)
  print(summ)


#n is row
#m in column
n=4
m=4
print(answer(n,m))