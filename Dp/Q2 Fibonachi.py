def fibonacchi(n):
  if n<=1:
    return n
  return fibonacchi(n-1) + fibonacchi(n-2)


# print(fibonacchi(5))

# momization
def dpFibo(dp,n):
  # print(n,"n")
  if dp[n]!=-1:
    # print("boom")
    return dp[n]
  dp[n] = dpFibo(dp,n-1)+dpFibo(dp,n-2)
  return dp[n]

def answer(n):
  dp = [-1]*(n+1)
  dp[0] = 0
  dp[1] = 1
  # print(dp)
  print(dpFibo(dp,n))

# answer(6)


# tabulation
def tabulation(n):
  dp = [-1]*(n+1)
  dp[0] = 0
  dp[1]=1
  for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
  print(dp[n])

# tabulation(6)



# space Optimizatoion

def Optimal(n):
  pre = 1
  pre2 = 0
  for i in range(2,n+1):
    curr = pre+pre2
    pre2 = pre
    pre = curr
  print(curr,pre)

Optimal(6)



