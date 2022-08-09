# def answer(index,summ,arr,dp):
#     if summ==0:
#         return True
#     if index==-1:
#         return False
#     if summ<0:
#         return False
#     if summ >= arr[index]:
#         if dp[index-1][summ-arr[index]]==-1:
#             dp[index-1][summ-arr[index]] = answer(index-1,summ-arr[index],arr,dp)
#         if dp[index-1][summ-arr[index]]:
#             return True
#     if dp[index-1][summ] == -1:
#         dp[index-1][summ] = answer(index-1,summ,arr,dp)
#     return dp[index-1][summ]


# def subsetSumToK(n, k, arr):
#     dp = []
#     for i in range(n):
#         temp=[]
#         for i in range(k+1):
#             temp.append(-1)
#         dp.append(temp)
#     ans =  answer(n-1,k,arr,dp)
#     print(dp)
#     return ans
    
    




def subsetSumToK(n, k, arr):
    dp=[]
    for i in range(n):
        temp = [False]*(k+1)
        dp.append(temp)
    for i in range(n):
        dp[i][0] = True
    if arr[0]<k:
        dp[0][arr[0]] = True
    for index in range(1,n):
        for summ in range(1,k+1):
            notTaken = dp[index-1][summ]
            taken = False
            if summ>=arr[index]:
                taken = dp[index-1][summ-arr[index]]
            dp[index][summ] = taken or notTaken
    print(dp)
    return dp[n-1][k]



n = 4
k= 4
arr=[6, 1 ,2 ,1]
subsetSumToK(n, k, arr)
n=5 
k = 6
arr = [1 ,7 ,2, 9, 10]
subsetSumToK(n, k, arr)
