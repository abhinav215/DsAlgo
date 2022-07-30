# def answer(index,nums,ans,n,lt):
#   if index==n:
#     # print(lt)
#     ans[0] = max(ans[0],len(lt))
#     return
#   print(index,lt,nums)
#   if lt==[] or nums[index]>lt[-1]:
#     answer(index+1,nums,ans,n,lt+[nums[index]])
#   answer(index+1,nums,ans,n,lt)
  


# def lengthOfLIS( nums):
#   ans = [0]
#   n = len(nums)
#   lt=[]
#   answer(0,nums,ans,n,lt)
#   print(ans)



# nums = [10,9,2,5,3,7,101,18]
# lengthOfLIS(nums)


# def answer(index,prevIndex,nums,n,dp):
#   if index==n:
#     return 0

#   if dp[index][prevIndex+1]!=-1:
#     return dp[index][prevIndex+1]
#   print("boom")
#   l = 0+answer(index+1,prevIndex,nums,n,dp)
#   if prevIndex==-1 or nums[index]>nums[prevIndex]:
#     l=max(l,1+answer(index+1,index,nums,n,dp))
#   dp[index][prevIndex+1] =l
#   return  l
  


# def lengthOfLIS( nums):
#   n = len(nums)
#   dp = []
#   for i in range(n):
#     temp = [-1]*(n+1)
#     dp.append(temp)
#   print(answer(0,-1,nums,n,dp))


# nums = [10,9,2,5,3,7,101,18]
# lengthOfLIS(nums)






  


def lengthOfLIS( nums):
  n = len(nums)
  dp = []
  for i in range(n+1):
    temp = [0]*(n+1)
    dp.append(temp)
    # print(temp)
  
  for index in range(n-1,-1,-1):
    for prevIndex in range(index-1,-2,-1):
      # print(index,prevIndex)
      l = 0+dp[index+1][prevIndex+1]
      if prevIndex==-1 or nums[index]>nums[prevIndex]:
        l=max(l,1+dp[index+1][index+1])
      dp[index][prevIndex+1] = l
  print(dp)
  return dp[0][0]



nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))