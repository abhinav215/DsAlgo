# Minimum number of platforms required for a railway
# Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

def shaping(s):
  h,m = list(map(int,s.split(":")))
  t= h*60+m
  return t

def answer(n,arr,dep):
  # for i in range(n):
  #   arr[i] = shaping(arr[i])
  # for i in range(n):
  #   dep[i] = shaping(dep[i])
  arr.sort()
  dep.sort()
  print(arr,dep)
  arrPointer = 1
  depPointer = 0
  count = 1
  maxi =1
  time = 1
  while arrPointer<n:
    if arr[arrPointer]>=dep[depPointer]:
      count-=1
      # print(count,dep[depPointer])
      depPointer+=1
    else:
      count+=1
      # print(count,arr[arrPointer],"ARR")
      arrPointer+=1
      if count>maxi:
        maxi=count
  # print(maxi)
  return maxi

  
  

N=6
# arr = ["9:00", "9:45", "9:55", "11:00", "15:00", "18:00"]
# dep = ["9:20", "12:00", "11:30", "11:50", "19:00", "20:00"]
arr = [900, 920, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130,1150,1900, 2000]
print(answer(N,arr,dep))