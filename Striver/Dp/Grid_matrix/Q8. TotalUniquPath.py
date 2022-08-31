# from os import *
# from sys import *
# from collections import *
# from math import *

# def answer(i,j,dp):
#     if i==0 and j==0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     up = answer(i-1,j,dp)
#     left = answer(i,j-1,dp)
#     dp[i][j] = up+left
#     return dp[i][j]


# def uniquePaths(m, n):
#     dp = []
#     for i in range(m):
#         temp = [-1]*n
#         dp.append(temp)
#     return answer(m-1,n-1,dp)










# def uniquePaths(m, n):
#     dp = []
#     for i in range(m+1):
#         temp = [0]*(n+1)
#         dp.append(temp)
#     dp[1][1] = 1
#     if n==1 or m==1:
#         return 1
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if i==1 and j==1:
#                 continue
#             up = dp[i-1][j]
#             left = dp[i][j-1]
#             dp[i][j] = up+left
#     return dp[m][n]












# def uniquePaths(m, n):
#     pre = [0]*n
#     for i in range(m):
#         temp=[0]*n
#         for j in range(n):
#             if i==0 and j==0:
#                 temp[j] = 1
#                 continue
#             if j==0:
#                 temp[j] = pre[j]
#                 continue
#             temp[j] = pre[j] + temp[j-1]
# #         print(temp)
#         pre = temp[:]
#     return temp[n-1]