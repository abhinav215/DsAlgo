
def isValid(a,b,c):
  if a>=b and a<c:
    return True
  return False

def rec(row,col,dir,vis,turn,s):
  # print(row,col,s[turn])
  if row==6 and col==0:
    if turn==48:
      return 1
    return 0
  if vis[row][col]!=0:
    return 0
  FourDir = [0]*4
  for k in range(4):
    if isValid(row+dir[k][0],0,7) and isValid(col+dir[k][1],0,7):
      FourDir[k] = vis[row+dir[k][0]][col+dir[k][1]]
  if not FourDir[1] and not FourDir[0] and FourDir[3] and FourDir[2]:
    return 0
  if FourDir[1] and FourDir[0] and not FourDir[3] and not FourDir[2]:
    return 0
  if isValid(row-1,0,7) and isValid(col+1,0,7) and vis[row-1][col+1]==1:
    if not FourDir[0] and not FourDir[3]:
      return 0
  if isValid(row+1,0,7) and isValid(col+1,0,7) and vis[row+1][col+1]==1:
    if not FourDir[0] and not FourDir[2]:
      return 0
  if isValid(row-1,0,7) and isValid(col-1,0,7) and vis[row-1][col-1]==1:
    if not FourDir[1] and not FourDir[3]:
      return 0
  if isValid(row+1,0,7) and isValid(col-1,0,7) and vis[row+1][col-1]==1:
    if not FourDir[1] and not FourDir[2]:
      return 0
  vis[row][col]=1
  numberOfPath = 0
  if s[turn]=="?":
    for k in range(4):
      # print("lalalalla",dir[k])
      if isValid(row+dir[k][0],0,7) and isValid(col+dir[k][1],0,7):
        numberOfPath+= rec(row+dir[k][0],col+dir[k][1],dir,vis,turn+1,s)
  elif s[turn]=="R" and col+1<7:
    print("R",row,col)
    numberOfPath+= rec(row,col+1,dir,vis,turn+1,s)
  elif s[turn]=="L" and col-1>=0:
    print("L",row,col)
    numberOfPath+= rec(row,col-1,dir,vis,turn+1,s)
  elif s[turn]=="U" and row-1>=0:
    print("U",row,col)
    numberOfPath+= rec(row+1,col,dir,vis,turn+1,s)
  elif s[turn]=="D" and row+1<7:
    print("D",row,col)
    numberOfPath+= rec(row-1,col,dir,vis,turn+1,s)
  vis[row][col]=0
  return numberOfPath





def answer(txt):
  dir = [[0,1],[0,-1],[1,0],[-1,0]]
  vis = []
  for i in range(7):
    temp = [0]*7
    vis.append(temp)
  print(rec(0,0,dir,vis,0,txt))


txt = "??????R??????U??????????????????????????LD????D?"
print(answer(txt))