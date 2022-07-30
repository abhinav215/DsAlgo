



def binarySearch(lt,target):
  n = len(lt)
  m =len(lt[0])
  left = 0
  right = m*n-1
  i=0
  while left<=right and i<10:
    mid = (right+left)//2
    # print(left,right,mid,"pointers")
    row = mid//m
    column = mid%m
    # print(row,column)
    if target == lt[row][column]:
      return ["YES",row,column]
    elif target > lt[row][column]:
      left = mid+1
    else:
      right=mid-1
    i+=1
  return ["NO"]









m = [[1,3,5,7],
 [10,11,16,17],
 [18,19,20,22],
 [23,30,34,60],
 [70,80,90,100]]
target = 3
print(binarySearch(m,target))
target = 11
print(binarySearch(m,target))
target = 19
print(binarySearch(m,target))
target = 30
print(binarySearch(m,target))
target = 80
print(binarySearch(m,target))