def contain(a):
  if a==7:
    return True

s=[1,2,3,4,5,6,7,8,9,17,77]
# a = map(summ,s)
for ele in s:
  if s%7==0 or map(contain,str(ele)):
    print(ele)