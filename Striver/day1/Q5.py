class Solution:
    def sortColors(self, nums):
        p0,p2 = 0,len(nums)-1
        p = 0
        while p<=p2:
            if nums[p]>1:
                nums[p],nums[p2] = nums[p2],nums[p]
                # p+=1
                p2-=1
            elif nums[p]<1:
                nums[p],nums[p0] = nums[p0],nums[p]
                p+=1
                p0+=1
            else:
                p+=1