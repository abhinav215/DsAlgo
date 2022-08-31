# import sys

# def answer(i,j,triangle,dp):
#     if i==len(triangle)-1:
#         return triangle[i][j]
#     if j<0:
#         return sys.maxsize
#     if dp[i][j]!= None:
#         return dp[i][j]
#     straight = triangle[i][j]+answer(i+1,j,triangle,dp)
#     diagonal = triangle[i][j]+answer(i+1,j+1,triangle,dp)
#     dp[i][j] = min(straight,diagonal)
#     return dp[i][j]


# def minimumPathSum(triangle, n):
#     # Write your code here.
#     dp = []
#     for i in range(n):
#         temp = [None]*n
#         dp.append(temp)
#     ans = answer(0,0,triangle,dp)
#     return ans








# import sys



# def minimumPathSum(triangle, n):
#     # Write your code here.
#     dp = []
#     for i in range(n):
#         temp = [None]*n
#         dp.append(temp)
    

#     for i in range(len(triangle)):
#         for j in range(i+1):
# #             print(i,j)
#             if i==0 and j==0:
#                 dp[i][j] = triangle[i][j]
#                 continue
#             if i==j:
#                 dp[i][j] = triangle[i][j]+dp[i-1][j-1]
#                 continue
#             if j == 0:
#                 dp[i][j] = triangle[i][j]+dp[i-1][j]
#                 continue
#             dp[i][j] = triangle[i][j]+min(dp[i-1][j-1],dp[i-1][j])
# #     print(dp)
#     return min(dp[len(triangle)-1])












import sys

def answer(i,j,triangle,dp):
    if i==len(triangle)-1:
        return triangle[i][j]
    if j<0:
        return sys.maxsize
    if dp[i][j]!= None:
        return dp[i][j]
    straight = triangle[i][j]+answer(i+1,j,triangle,dp)
    diagonal = triangle[i][j]+answer(i+1,j+1,triangle,dp)
    dp[i][j] = min(straight,diagonal)
    return dp[i][j]


def minimumPathSum(triangle, n):
    # Write your code here.
#     dp = []
#     for i in range(n):
#         temp = [None]*n
#         dp.append(temp)
    dp = [None]*n
    

    for i in range(len(triangle)):
        temp = [None]*n
        for j in range(i+1):
#             print(i,j)
            if i==0 and j==0:
                temp[j] = triangle[i][j]
                continue
            if i==j:
                temp[j] = triangle[i][j]+dp[j-1]
                continue
            if j == 0:
                temp[j] = triangle[i][j]+dp[j]
                continue
            temp[j] = triangle[i][j]+min(dp[j-1],dp[j])
        dp = temp[:]
#         print(dp)
    return min(dp)