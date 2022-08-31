def answer(n,src,mid,des):
  if n>0:
    answer(n-1,src,des,mid)
    print(src,des)
    answer(n-1,mid,src,des)

n = int(input())
print(2**n-1)
answer(n,1,2,3)