def Listmaker(n):
  lt =[]
  for i in range(n):
    lt.append(0)
  return lt

def ValidQ(row,col,hash1,hash2,hash3):
  if hash1[row]==1:
    return False
  if hash2[row+col]==1:
    return False
  if hash3[(n-1)+(col-row)]==1:
    return False
  return True


def converter(lt):
  ans =[]
  n = len(lt)
  for j in range(n):
    out=""
    for i in range(n):
      out+=lt[j][i]
    ans.append(out)
  return ans
  


def answer(index,n,lt,ans,hash1,hash2,hash3):
  if index==n:
    ss = converter(lt)
    ans.append(ss)
    print("lt",ss,ans)
    return
  for i in range(n):
    # print(ValidQ(i,index,hash1,hash2,hash3),i,index)
    if ValidQ(i,index,hash1,hash2,hash3):
      lt[i][index]="Q"
      hash1[i]=1
      hash2[i+index]=1
      hash3[(n-1)+(index-i)]=1
      # print(i,index,lt)
      # print("hash",hash1,hash2,hash3)
      answer(index+1,n,lt,ans,hash1,hash2,hash3)
      lt[i][index]="."
      hash1[i]=0
      hash2[i+index]=0
      hash3[(n-1)+(index-i)]=0
    


def solveNQueens(n):
  lt =[]
  for i in range(n):
    temp =[]
    for j in range(n):
      temp.append(".")
    lt.append(temp)
  # print(lt)
  ans =[]
  hash1 = Listmaker(n)
  hash2 = Listmaker(2*n-1)
  hash3 = Listmaker(2*n-1)
  # print(hash1,hash2,hash3)
  answer(0,n,lt,ans,hash1,hash2,hash3)
  print(ans)
  return ans


n=4
solveNQueens(n)