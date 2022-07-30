


def ans(m):
  r = len(m)
  c = len(m[0])
  top = 0
  down = r-1
  left = 0
  right = c-1
  dir = 0 
  # 0 means right
  # 1 means down
  # 2 means left
  # 3 means up
  output= ""
  # print(left,right,down ,top)
  while top<=down and left<=right:
    if dir ==0:
      for i in range(left,right+1):
        output += str(m[top][i])
        output += " "
      top+=1
    elif dir ==1:
      for i in range(top,down+1):
        output += str(m[i][right])
        output += " "
      right-=1
    elif dir ==2:
      for i in range(right,left-1,-1):
        output += str(m[down][i])
        output += " "
      down-=1
    elif dir ==3:
      for i in range(down,top-1,-1):
        output += str(m[i][left])
        output += " "
      left+=1
    dir=(dir+1)%4
    # print("emergency",left,right,down ,top)
    # print("output=" , output)
  print(output)





m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans(m)