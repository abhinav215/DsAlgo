
def answer(lt,target):
  n = len(lt)
  m = len(lt[0])
  i=0
  j = m-1
  while True:
    if lt[i][j]==target:
      return ["YES",i,j]
    if lt[i][j]>target:
      j-=1
    else:
      i+=1
    if i==n:
      return ["NO"]
    if j==-1:
      return ["NO"]



m=[[10,20,30,40],[11,21,36,43],[25,29,39,50],[51,60,70,80]]
target = 36
print(answer(m,target))
target = 60
print(answer(m,target))
target = 22
print(answer(m,target))
target = 100
print(answer(m,target))