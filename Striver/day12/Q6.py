
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

  def getMax(self,x):
    res = ""
    size=32
    xInB = '{:032b}'.format(x)
    currentNode = self
    for i in range(size):
      finding = Compliment(xInB[i])
      if finding in currentNode.child:
        res += "1"
        currentNode=currentNode.child[finding]
      else:
        res += "0"
        currentNode = currentNode.child[xInB[i]]
    # print(res)
    ans = binToDeci(res)
    return ans




def Compliment(ele):
  if ele == "1":
    return "0"
  return "1"



def binToDeci(binary_num):
  # binary_num = input('Enter a binary string:')
  dec_num = int(binary_num, 2)
  return dec_num



def findMaximumXOR(arr):
  #insert All element of arr in Trie
  trie = Trie()
  for ele in arr:
    xInB = '{:032b}'.format(ele)
    trie.insert(xInB)
  maxi = 0
  for ele in arr:
    count = trie.getMax(ele)
    # print(count,ele)
    maxi = max(maxi,count)
  print(maxi)
  return maxi





# num = [3,10,5,25,2,8]
num = [14,70,53,83,49,91,36,80,92,51,66,70]
findMaximumXOR(num)