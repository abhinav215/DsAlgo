import heapq

def answer(nums,k):
  heapq.heapify(nums)
  print(nums)
  # nlargest = heapq.nlargest(k,nums)
  print(heapq.nlargest(k,nums)[-1])






nums = [3,2,1,5,6,4]
k = 2
print(answer(nums,k))