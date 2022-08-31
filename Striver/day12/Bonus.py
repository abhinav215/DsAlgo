# find max(x exor arr[i])


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


def Compliment(ele):
  if ele == "1":
    return "0"
  return "1"



def binToDeci(binary_num):
  # binary_num = input('Enter a binary string:')
  dec_num = int(binary_num, 2)
  return dec_num



def deciToBin( dec_num):
  # dec_num = int(input('Enter a decimal number:'))
  binary_num= bin(dec_num).replace('0b', '')
  return binary_num



def maxingExor(arr,x):
  trie = Trie()
  for ele in arr:
    xInB = '{:032b}'.format(ele)
    trie.insert(xInB)

  res = ""
  size=32

  xInB = '{:032b}'.format(x)
  currentNode = trie
  for i in range(size):
    finding = Compliment(xInB[i])
    if finding in currentNode.child:
      res += "1"
      currentNode=currentNode.child[finding]
    else:
      res += "0"
      currentNode = currentNode.child[xInB[i]]
  print(res)
  print(binToDeci(res))

    

  





arr = [9,8,7,5,4]
x = 8
maxingExor(arr,x)