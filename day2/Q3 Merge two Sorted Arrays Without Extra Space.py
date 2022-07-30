
import math


def answer(n,lt1,m,lt2):
  lt = lt1+lt2
  print(lt)
  lt.sort()
  ans1 =  lt[0:n]
  ans2 =  lt[n:]
  print(ans1,ans2)

def swap(a,b):
  temp = a
  a = b
  b = temp
  return [a,b]

def answer2(n,lt1,m,lt2):
  i = 0 
  j = 0
  for i in range(n):
    flag = 0
    # print(lt1[i],lt2[0])
    if lt1[i]>lt2[0]:
      lt1[i],lt2[0] = swap(lt1[i],lt2[0])
      flag = 1
    # print(lt1)
    change = lt2[0]
    # print(lt2,m)
    for j in range(m):
      if lt2[j]>change and flag==1:
        print("j",j)
        lt2[j-1],lt2[0]= change,lt2[j-1]
        flag =0
        break
    if flag == 1:
      lt2[m-1],lt2[0]= change,lt2[m-1]
    print(i, lt1,lt2)
  pass

#gap method
def answer3(n,lt1,m,lt2):
  gap = math.ceil((n+m)/2)
  # print(gap)
  while gap<=1:
    for i in range(n):
      pass


n = 4
arr1 = [1, 4, 8 ,10] 
m = 3
arr2 = [2, 3 ,9]

# n = 4
# arr1 = [1 ,3, 5, 7] 
# m = 5
# arr2= [0, 2, 6 ,8 ,9]
print(arr1,arr2)
answer2(n,arr1,m,arr2)