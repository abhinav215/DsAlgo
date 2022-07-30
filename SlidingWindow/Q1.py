from collections import deque


# arr = 2,3,5,2,9,7,1
# k = 3
# find sub array of size k with max summ of element of sub array


def answer(lt,k):
  n = len(lt)
  summ = lt[0]+lt[1]+lt[2]
  res=[lt[0],lt[1],lt[2]]
  maxx = summ
  for i in range(3,n):
    summ -= lt[i-3]
    summ += lt[i]
    if summ>maxx:
      maxx = max(maxx,summ)
      res = [lt[i-2],lt[i-1],lt[i]]
  print(maxx)
  print(res)



arr = [2, 3 ,4 ,5 ,2 ,9, 7, 1]
k = 3
answer(arr,k)