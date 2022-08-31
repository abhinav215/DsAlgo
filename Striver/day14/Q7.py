class StockSpanner:

  def __init__(self):
    self.st = []
    self.arr = []
    self.index= 0

  def next(self, price: int) -> int:
    self.index+=1
    # print(self.st,self.arr)
    while self.st != [] and self.arr[self.st[-1]-1]<=price:
      self.st.pop()
      # print(self.st,"pop")
    if self.st ==[]:
      ans = 1
    else:
      ans = self.index - self.st[-1]
    self.st.append(self.index)
    self.arr.append(price)
    print(ans)
    return ans


stockSpanner = StockSpanner()
stockSpanner.next(100)
stockSpanner.next(80)
stockSpanner.next(60)
stockSpanner.next(70)
stockSpanner.next(60)
stockSpanner.next(75)
stockSpanner.next(85)


# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6