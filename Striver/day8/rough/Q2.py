# Minimum number of platforms required for a railway
# Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. We need to find the minimum number of platforms needed at the railway station so that no train has to wait.


def shaping(s):
  h,m = list(map(int,s.split(":")))
  # print(s,"S",h,m)
  t= h*60+m
  return t

def listing(a,b):
  a = shaping(a)
  b = shaping(b)
  ele = [a,b]
  return ele


def platform(lt,n):
  arrpointer = 1
  deppointer = 0
  count=1
  maxi=1
  while arrpointer<n:
    print("count",count,arrpointer,deppointer,lt[arrpointer][0],lt[deppointer][1])
    if lt[arrpointer][0]>lt[deppointer][1]:
      count+=1
      deppointer+=1
      if count>maxi:
        maxi=count
    else:
      count-=1
      arrpointer+=1
  print(maxi)


def answer(n,arr,dep):
  lt= list(map(listing,arr,dep))
  print(lt)
  lt = sorted(lt,key = lambda x:x[1])
  print(lt)
  return platform(lt,n)






N=6
arr = ["9:00", "9:45", "9:55", "11:00", "15:00", "18:00"]
dep = ["9:20", "12:00", "11:30", "11:50", "19:00", "20:00"]
print(answer(N,arr,dep))