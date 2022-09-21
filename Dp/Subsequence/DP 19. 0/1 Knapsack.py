
def answer(n,wt,val,maxWt):
    dp=[]
    for i in range(n):
        temp = [-1]*(maxWt+1)
        dp.append(temp)
#     print(dp)
    
    def rec(index,totalWt,TotalVal,dp):
        if index==0:
            if totalWt>=wt[index]:
                TotalVal += val[index]
                return val[index]
            return 0
#         print(index,totalWt,len(dp),len(dp[0]))
        if dp[index][totalWt]!=-1:
            return dp[index][totalWt]
        #notpick
        notpick = rec(index-1,totalWt,TotalVal,dp)
        #pick
        pick = -10000
        if totalWt>=wt[index]:
            pick = val[index] + rec(index-1,totalWt-wt[index],TotalVal+val[index],dp)
        dp[index][totalWt]= max(pick,notpick)
        return dp[index][totalWt]
    
    return rec(n-1,maxWt,0,dp)
#     return dp[n-1][0]


t= int(input())
for u in range(t):
    n = int(input())
    txt = input()
    wt = list(map(int,txt.split()))
    txt = input()
    val = list(map(int,txt.split()))
    maxWt = int(input())
    print(answer(n,wt,val,maxWt))