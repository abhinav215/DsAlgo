


def findMedianSortedArrays(arr1,arr2):
  n1= len(arr1)
  n2=len(arr2)
  if n1>n2:
    return findMedianSortedArrays(arr2,arr1)
  
  low = 0
  high = n1
  print(low,high)
  while low<=high:

    cut1 = (low+high)//2
    cut2 = (n1+n2+1)//2-cut1

    
    print(low,cut1,high)

    l1 = -10000 if  cut1==0 else arr1[cut1-1]
    l2 = -10000 if  cut2==0 else arr2[cut2-1]

    r1 = 10000000 if cut1 == n1 else arr1[cut1]
    r2 = 10000000 if cut2 == n2 else arr2[cut2]

    if l1<=r2 and l2<=r1:
      if (n1+n2)%2==0:
        print((max(l1,l2)+min(r1,r2))/2)
        return (max(l1,l2)+min(r1,r2))/2
      print(max(l1,l2))
      return max(l1,l2)
    elif l1>r2:
      high = cut1-1
    else:
      low=cut1+1


  if (n1+n2)%2==0:
    # print(arr2[(n2-1)//2], max(arr1[0],arr2[((n2-1)//2)-1]))
    ans = (arr2[(n2-1)//2]+ max(arr1[0],arr2[((n2-1)//2)-1]))/2
    print(ans)
    return ans
  ans = max(arr1[0],arr2[(n2-1)//2])
  print(ans,"ans")
  return ans



arr1=[1,3,4,7,10,12]
arr2=[2,3,6,15]
#(4+6)//2=5


# arr1=[1,3,4]
# arr2=[2]


# arr1=[1,2]
# arr2=[3,4]
findMedianSortedArrays(arr1,arr2)
