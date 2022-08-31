# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Input: nums = [100,4,200,1,3,2]
# Output: 4

def answer(lt):
  n= len(lt)
  lt.sort()
  print(lt)
  maxi = 1
  count=1
  for i in range(n-1):
    if lt[i+1]-lt[i]==0:
      continue
    # print(lt[i+1],lt[i])
    elif lt[i+1]-lt[i]==1:
      count+=1
      print(count,lt[i+1])
      if maxi<count:
        maxi = count
    else:
      count = 1
  print(maxi)
  return maxi



# nums = [100,4,200,1,3,3,2]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
answer(nums)