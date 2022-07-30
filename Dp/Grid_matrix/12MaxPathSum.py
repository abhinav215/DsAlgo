# from sys import stdin, setrecursionlimit
# setrecursionlimit(10**7)

# import sys

# def answer(i,j,matrix,dp):
# #     print(i,j)
#     if j<0 or j>=len(matrix[0]):
#         return -sys.maxsize
#     if i==0:
#         return matrix[i][j]
#     if dp[i][j]!= None:
#         return dp[i][j]
#     maxi = -sys.maxsize
#     maxi = max(maxi,answer(i-1,j-1,matrix,dp))
#     maxi = max(maxi,answer(i-1,j,matrix,dp))
#     maxi = max(maxi,answer(i-1,j+1,matrix,dp))
#     dp[i][j] = maxi + matrix[i][j]
#     return dp[i][j]
    
    
# def getMaxPathSum(matrix):
#     n = len(matrix)
#     m  = len(matrix[0])
#     dp = []
#     for i in range(n):
#         temp = [None]*m
#         dp.append(temp)
        
#     maxi = -sys.maxsize
#     for i in range(m):
#         maxi = max(maxi,answer(n-1,i,matrix,dp))
#     return maxi






    
# def getMaxPathSum(matrix):
#     n = len(matrix)
#     m  = len(matrix[0])
#     dp = matrix[0][:]
#     for i in range(1,n):
#         temp = [None]*m
#         for j in range(m):
# #             print(i,j)
#             dl = dr = -sys.maxsize
#             if j>0:
#                 dl = dp[j-1]
#             if j<m-1:
#                 dr = dp[j+1]
# #             print(dl,dp[j],dr,i,j,matrix[i][j])
#             temp[j] = matrix[i][j] + max(dl,dp[j],dr)
#         dp = temp[:]
# #         print(dp)
#     return max(dp)
        