class Solution:
    def nextPermutation(self, a) -> None:
      n = len(a)
      index1 = -1
      for i in range(n-2,-1,-1):
        if a[i]<a[i+1]:
          index1 = i
          break
      if index1==-1:
        a.reverse()
        return
      for i in range(n-1,index1,-1):
        if a[index1]<a[i]:
          a[index1],a[i]=a[i],a[index1]
          break
      print(a,a[:index1+1],a[n-1:index1:-1])
      length = n-index1
      pos = index1+1
      for i in range(length//2):
        a[pos+i],a[n-1-i] = a[n-1-i],a[pos+i]
      
        