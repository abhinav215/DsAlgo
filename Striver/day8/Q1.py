N = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]

def answer(lt,n):
  count = 1
  i=0
  for j in range(1,n):
    if lt[i][1]<lt[j][0]:
      count+=1
      i=j
  return count

def listing(a,b):
  ele = [a,b]
  return ele

def maximumMeetings(n,start,end):
  lt= list(map(listing,start,end))
  lt = sorted(lt,key = lambda x:x[1])
  print(lt)
  return answer(lt,n)




# N = 8
# start = [75250, 50074, 43659, 8931, 11273, 27545, 50879 ,77924]
# end =  [112960 ,114515 ,81825 ,93424 ,54316 ,35533, 73383, 160252]
print(maximumMeetings(N,start,end))