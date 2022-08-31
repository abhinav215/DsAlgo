# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.


def answer(lt,n):
  dic={0:-1}
  summ = 0
  maxi = 0
  for i in range(n):
    summ += lt[i]
    if summ in dic:
      newCount = (i-dic[summ])
      if newCount>maxi:
        maxi = newCount
    else:
      dic[summ]=i
  print(dic)
  print(maxi)


# N = 8
# A= [15,-2,2,-8,1,7,10,23]
N=10
A=[1,-1,3,2,-2,-8,1,7,10,23]
print(answer(A,N))