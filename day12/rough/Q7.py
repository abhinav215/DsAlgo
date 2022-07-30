
class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    self.isEnd = False
    self.count = 0
    #dictionary with key as character and value as node
    self.child={}
      

  def insert(self, word: str) -> None:
    currentNode = self
    size = 32
    for i in range(size):
      if word[i] not in currentNode.child:
        currentNode.child[word[i]] = Trie(word[i])
      currentNode=currentNode.child[word[i]]
    currentNode.isEnd = True
    currentNode.count += 1


  def getMax(self,x,m):
    res = ""
    change=0
    size=32
    xInB = '{:032b}'.format(x)
    mInB = '{:032b}'.format(m)
    # print(xInB)
    # print(mInB)
    # print("---------------")
    currentNode = self
    for i in range(size):
      finding = Compliment(xInB[i])
      if change==0 and mInB[i]=="0":
        res += str(0^int(xInB[i]))
        if "0" in currentNode.child:
          currentNode = currentNode.child["0"]
        else:
          return -1
      elif finding in currentNode.child:
        res += "1"
        currentNode=currentNode.child[finding]
        if finding =="0" and mInB[i] == "1":
          change=1
      else:
        res += "0"
        currentNode = currentNode.child[xInB[i]]
        if finding =="1" and mInB == "1":
          change=1
      
    # print(res)
    ans = binToDeci(res)
    # print(ans)
    return ans


def Compliment(ele):
  if ele == "1":
    return "0"
  return "1"



def binToDeci(binary_num):
  # binary_num = input('Enter a binary string:')
  dec_num = int(binary_num, 2)
  return dec_num



#queries =[xi,mi] = xi is number and mi is max

def maximizeXor(arr,queries):
  #insert All element of arr in Trie
  trie = Trie()
  for ele in arr:
    xInB = '{:032b}'.format(ele)
    trie.insert(xInB)
  ans = []
  for ele in queries:
    count = trie.getMax(ele[0],ele[1])
    # print(count,ele)
    ans.append(count)
    # break
  print(ans)
  return ans




# nums = [0,1,2,3,4]
# queries = [
#         [3,1],
#         [1,3],
#         [5,6]]


nums = [5,2,4,6,6,3]
queries = [[12,4],[8,1],[6,3]]
maximizeXor(nums,queries)