class Solution:
    def maxProfit(self, prices) -> int:
        lt = []
        for i in range(1,len(prices)):
            lt.append(prices[i]-prices[i-1])
        print(lt)
        maxi = 0
        profit = 0
        for ele in lt:
            profit+=ele
            if profit<0:
                profit=0 
            else:
                maxi = max(maxi,profit)
        return maxi