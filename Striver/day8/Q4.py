
# ITEMS contains [weight, value]


def maximumValue(item,n,w):
  lt=[]
  for i in range(n):
    lt.append([item[0][i],item[1][i]])
  print(lt)
  lt = sorted(lt,key = lambda x:(x[0]/x[1]))
  print(lt)
  val = 0
  for i in range(n):
    if w-lt[i][0]<0:
      leftover = w * lt[i][1]/lt[i][0]
      ans = float(leftover+val)
      print(ans)
      ans = "{:.2f}".format(ans)
      return ans
    w -= lt[i][0]
    val+=lt[i][1]
    if w==0:
      ans = float(val)
      ans = "{:.2f}".format(ans)
      print
      return ans





n = 4
w = 6
item = [[6, 1, 5, 3],[3, 6, 1, 4]]

# n = 3 
# w=50
# item = [[10,20,30],[60,100,120]]

print(maximumValue(item,n,w))