class Solution:
    def maxSubArray(self, nums) -> int:
        summ = 0
        maxi = -sys.maxsize
        for ele in nums:
            summ+=ele
            maxi = max(summ,maxi)
            if summ<0:
                summ = 0
        return maxi