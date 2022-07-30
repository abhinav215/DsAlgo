


def kthsorted(arr1,arr2,k):
  n1 = len(arr1)
  n2 = len(arr2)
  if n1>n2:
    return kthsorted(arr2,arr1,k)
  low = 0
  high=n1
  while low<=high:
    cut1 = (low+high)//2
    cut2 = k-cut1

    if cut2>=n2:
      low = cut1+1
    else:
      print(low,cut1,high,cut2)

      l1 = -10000 if cut1==0 else arr1[cut1-1]
      l2 = -10000 if cut2==0 else arr2[cut2-1]

      r1 = 100000 if cut1==n1 else arr1[cut1]
      r2 = 100000 if cut2==n2 else arr2[cut2]

      if l1<=r2 and l2<=r1:
        print( max(l1,l2))
        return max(l1,l2)
      elif l1>r2:
        high = cut1-1
      else:
        low = cut1+1





# array1 = [2,3,6,7,9]
# array2 = [1,4,8,10]
# k = 5

# array1 = [100, 112, 256, 349, 770]
# array2 = [72, 86, 113, 119, 265, 445, 892]
# k = 7


k=15
array1 =[ 1 ,10, 10 ,25, 40, 54, 79]
array2 =[ 15, 24, 27, 32, 33, 39 ,48 ,68 ,82, 88 ,90]

kthsorted(array1,array2,k)