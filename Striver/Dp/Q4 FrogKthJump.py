import sys

# def answer(index,k,h,dp):
#     if index<0:
#         return sys.maxsize
#     if index==0:
#         dp[0] = 0
#         return 0
#     mini = sys.maxsize
#     print(index,k,h,dp)
#     for i in range(1,k+1):
#         mini = min(mini,answer(index-i,k,h,dp)+ abs(h[index]-h[index-i]))
#         if index==4:
#             print(answer(index-i,k,h,dp),abs(h[index]-h[index-i]),h[index-i])
#             print(index,i,mini)
#             print("===========================")
#     dp[index] = mini
#     return mini


# def frogJump(n,h,k):
#     print(h)
#     dp = [-1]*n
#     answer(n-1,k,h,dp)
#     print(dp)
#     print(dp[n-1])


# n,k=5 ,3
# height = [10 ,30, 40, 50, 20]
# print(frogJump(n,height,k))










# def answer(index,k,h,dp):
#     if index<0:
#         return sys.maxsize
#     if index==0:
#         dp[0] = 0
#         return 0
#     if dp[index]!=-1:
#         return dp[index]
#     mini = sys.maxsize
#     # print(index,k,h,dp)
#     for i in range(1,k+1):
#         mini = min(mini,answer(index-i,k,h,dp)+ abs(h[index]-h[index-i]))
#         if index==4:
#             print(answer(index-i,k,h,dp),abs(h[index]-h[index-i]),h[index-i])
#             print(index,i,mini)
#             print("===========================")
#     dp[index] = mini
#     return mini


# def frogJump(n,h,k):
#     print(h)
#     dp = [-1]*n
#     answer(n-1,k,h,dp)
#     print(dp)
#     print(dp[n-1])


# n,k=5 ,3
# height = [10 ,30, 40, 50, 20]
# print(frogJump(n,height,k))













# def frogJump(n,h,k):
#     dp = [-1]*(n)
#     dp[0] = 0
#     for i in range(1,k+1):
#         mini = sys.maxsize
#         for j in range(i):
#             # print(i,j,)
#             mini = min(mini,dp[j]+abs(h[i]-h[j]))
#         dp[i] = mini

#     print(dp)
#     for i in range(k+1,n):
#         mini = sys.maxsize
#         for j in range(1,k+1):
#             print(h[j],i,j,dp[j],abs(h[i]-h[j]))
#             mini = min(mini,dp[i-j]+abs(h[i]-h[i-j]))
#         dp[i] = mini
#     print(dp)



# n,k=5 ,3
# height = [10 ,30, 40, 50, 20]
# print(frogJump(n,height,k))



from collections import deque 

def frogJump(n,h,k):
    dp = [-1]*(k)
    dp[0] = 0
    for i in range(1,k):
        mini = sys.maxsize
        for j in range(i):
            # print(i,j)
            mini = min(mini,dp[j]+abs(h[i]-h[j]))
        dp[i] = mini
    dp = deque(dp)
    # print(dp)
    for i in range(k,n):
        mini = sys.maxsize
        for j in range(k):
            mini = min(mini,dp[k-j-1]+abs(h[i]-h[k-j-1]))
        dp.popleft()
        dp.append(mini)
    print(dp)



n,k=5 ,3
height = [10 ,30, 40, 50, 20]
print(frogJump(n,height,k))
