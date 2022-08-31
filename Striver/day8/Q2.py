

def minimumPlatform(n,arr,dep):
  arr.sort()
  dep.sort()
  print(arr,dep)
  arrpointer = 0
  deppointer= 0
  count = maxi = 0
  while arrpointer<n:
    if arr[arrpointer] <= dep[deppointer]:
      count+=1
      maxi = max(maxi,count)
      arrpointer+=1
    else:
      count-=1
      deppointer+=1
    print(count)
  return maxi





N=6
# arr = ["9:00", "9:45", "9:55", "11:00", "15:00", "18:00"]
# dep = ["9:20", "12:00", "11:30", "11:50", "19:00", "20:00"]
arr = [900, 920, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130,1150,1900, 2000]
print(minimumPlatform(N,arr,dep))