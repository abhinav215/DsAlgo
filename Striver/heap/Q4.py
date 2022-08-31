import heapq

class MedianFinder:

    def __init__(self):
        self.half1 = []
        self.half2 = []
        self.size = 0
        heapq.heapify(self.half1)
        heapq.heapify(self.half2)
        
        

    def addNum(self, num: int) -> None:
        if len(self.half1)==len(self.half2):
            # print("even")
            if len(self.half1)!=0 and num>heapq.nsmallest(1,self.half2)[0]:
                x = heapq.heappop(self.half2)
                heapq.heappush(self.half2,num)
                heapq.heappush(self.half1,-1*x)
                self.size +=1
                return
            heapq.heappush(self.half1,-1*num)
        else:
            if num < -1*heapq.nsmallest(1,self.half1)[0]:
                x = heapq.heappop(self.half1)*-1
                heapq.heappush(self.half1,-1*num)
                heapq.heappush(self.half2,x)
                # print(x,"lol")
                self.size +=1
                return
            heapq.heappush(self.half2,num)
        self.size+=1
        

    def findMedian(self) -> float:
        # print(self.half1,self.half2)
        if self.size&1==1:
            # print(heapq.nlargest(1,self.half1)[0])
            return heapq.nsmallest(1,self.half1)[0]*-1
        # print(heapq.nlargest(1,self.half1)[0],heapq.nsmallest(1,self.half2)[0])
        return (-1*heapq.nsmallest(1,self.half1)[0]+heapq.nsmallest(1,self.half2)[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()