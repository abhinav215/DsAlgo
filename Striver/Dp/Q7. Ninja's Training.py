# from typing import *

# def answer(index,points,flag,dp):
#     if index==0:
#         maxi = 0
#         for i in range(3):
#             if i != flag:
#                 maxi = max(maxi,points[0][i])
#         return maxi
#     if dp[index][flag]!=-1:
#         return dp[index][flag]
#     maxi = 0
#     for i in range(3):
#         if i != flag:
#             maxi = max(maxi,points[index][i]+answer(index-1,points,i,dp))
#     dp[index][flag]=maxi
#     return maxi

  
# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     dp = []
#     for i in range(n):
#         temp = [-1]*4
#         dp.append(temp)
        
#     ans = answer(n-1,points,3,dp)
#     return ans









# from typing import *


# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     dp = []
#     for i in range(n):
#         temp = [-1]*4
#         dp.append(temp)
# #     print(dp)
    
#     for i in range(4):
#         maxi = 0
#         for j in range(3):
#             if i!=j:
#                 maxi = max(maxi,points[0][j])
#         dp[0][i] = maxi
# #     print(dp[0])
#     for k in range(1,n):
#         for last in range(4):
#             for task in range(3):
#                 if last!=task:
#                     dp[k][last] = max(dp[k][last] , points[k][task]+dp[k-1][task])
        
# #     print(dp)
#     return dp[n-1][3]












# from typing import *


# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     dp = [-1,-1,-1,-1]
#     for i in range(4):
#         maxi = 0
#         for j in range(3):
#             if i!=j:
#                 maxi = max(maxi,points[0][j])
#         dp[i] = maxi
#     ans = [-1,-1,-1,-1]
#     for k in range(1,n):
#         for last in range(4):
#             maxi = 0
#             for task in range(3):
#                 if last!=task:
#                     maxi = max(maxi , points[k][task]+dp[task])
#             ans[last] = maxi
#         dp = ans[:]
# #     print(dp)
#     return ans[3]
