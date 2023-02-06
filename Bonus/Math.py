# Given a Bucket having a capacity of N litres and the task is to determine that by how many ways you can fill it using two bottles of capacity of 1 Litre and 2 Litre only. Find the answer modulo 108.

# Input:
# 4
# Output:
# 5 
# Explanation:
# Let O denote filling by 1 litre bottle and
# T denote filling by 2 litre bottle.
# So for N = 4, we have :
# {TT,OOOO,TOO,OTO,OOT} thus there are 5 total ways.



def fillingBucket( N):
    dp = [-1]*(N+3)
    MOD = 10**8
    
    def solve(n):
        print(n)
        if n==0:
            return 1
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        dp[n] = (solve(n-1)+solve(n-2))%MOD 
        return dp[n]
    
    return solve(N)


fillingBucket(8223)