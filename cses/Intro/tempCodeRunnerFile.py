
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