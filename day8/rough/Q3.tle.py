# Test Cases Passed: 
# 164 /  215

# Time Limit Exceeded


# Your program took more time than expected.Time Limit Exceeded
# Expected Time Limit 8.16sec
# Hint : Please optimize your code and submit again.



class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs=sorted(Jobs, key=lambda x:-(x.profit))
        # prining(Jobs)
        # print(Jobs[0].profit)
        # print(Jobs[1].profit)
        number = 0
        for i in range(n):
            number = max(number,Jobs[i].deadline)
        ans = []
        for i in range(number):
            ans.append(-1)
        # print(ans)
        # print(Jobs[0].deadline)
        count = 0
        paisa = 0
        for i in range(n):
            k=0
            while Jobs[i].deadline-1-k>=0:
                if ans[Jobs[i].deadline-1-k] ==-1:
                    ans[Jobs[i].deadline-1-k]=Jobs[i].id
                    count+=1
                    paisa+=Jobs[i].profit
                    break
                k+=1
        return [count , paisa]