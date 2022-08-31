# Given an array of integers A and an integer B.

# Find the total number of subarrays having bitwise XOR of all elements equals to B.


def answer(lt,target):
  x = 0
  count = 0
  n = len(lt)
  dic={}
  for i in range(n):
    x = x ^ lt[i]
    y = x^target
    print(lt[i],target,y,"lnao")
    if x==target:
      print("increase count by 1")
      count+=1
    if y in dic:
      print("increase count by dic[y] =",dic[y])
      count+=dic[y]
    if x in dic:
      dic[x]+=1
    else:
      dic[x]=1
    print(lt[i],x,y,count)
  print(count)
  print(dic)



A = [4, 2, 2, 6, 4]
B = 6
answer(A,B)