from typing import List

# def answer(index,num,tar,dp):
#     if tar==0:
#         return 1
#     if index==0:
#         if num[index]==tar:
#             return 1
#         return 0
#     if dp[index][tar]!=-1:
#         return dp[index][tar]
#     notPick = answer(index-1,num,tar,dp)
#     pick = 0
#     if num[index]<=tar:
#         pick = answer(index-1,num,tar-num[index],dp)
#     dp[index][tar] = pick+notPick
#     return dp[index][tar]

# def findWays(num: List[int], tar: int) -> int:
#     n = len(num)
#     dp=[]
#     for i in range(n):
#         temp = [-1]*(tar+1)
#         dp.append(temp)
#     return answer(n-1,num,tar,dp)




# def findWays(num: List[int], tar: int) -> int:
#     n = len(num)
#     dp=[]
#     for i in range(n):
#         temp = [0]*(tar+1)
#         dp.append(temp)
#     for index in range(n):
#         dp[index][0] = 1
#     for t in range(tar+1):
#         if dp[0]==tar:
#             dp[0][t]=1
#         dp[0][t]=0
    
#     for index in range(n):
#         for t in range(tar+1):
#             notPick = dp[index-1][t]
#             pick = 0
#             if num[index]<=t:
#                 pick = dp[index-1][t-num[index]]
#             dp[index][t] = pick+notPick
#     # print(dp)
#     return dp[n-1][tar]



# def findWays(num: List[int], tar: int) -> int:
#     n = len(num)
#     prev = [0]*(tar+1)
#     cur = [0]*(tar+1)
#     prev[0] = 1
#     cur[0] = 1
    
#     if num[0]<=tar:
#         prev[num[0]]=1
    
#     print(prev)
#     for index in range(1,n):
#         for t in range(tar+1):
#             notPick = prev[t]
#             pick = 0
#             if num[index]<=t:
#                 pick = prev[t-num[index]]
#             cur[t] = pick+notPick
#         prev = cur[:]
#         print(prev)
#     return prev[tar]


num = [19,1,1]
tar = 4
# findWays(num, tar)