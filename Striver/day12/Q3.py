class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    self.isEnd = False
    self.endCount = 0
    #dictionary with key as character and value as node
    self.child={}
      
  
  def insert(self, word: str) -> None:
    currentNode = self
    for ele in word:
      if ele not in currentNode.child:
        # print(ele)
        currentNode.child[ele] = Trie(ele)
      currentNode=currentNode.child[ele]
    currentNode.isEnd = True
    currentNode.endCount += 1

  def check(self,word):
    currentNode = self
    for ele in word:
      if ele not in currentNode.child:
        return 0
      if not currentNode.child[ele].isEnd:
        return 0
      currentNode = currentNode.child[ele]
    return len(word)



def completeString(n: int, a)-> str:
  trie = Trie()
  for ele in a:
    trie.insert(ele)
  maxi = 0
  res = 0
  for ele in a:
    count = trie.check(ele)
    print(count)
    if count > maxi:
      maxi = count
      res = ele
  return res


n = 6
A = ["n", "ni" ,"nin", "ninj","ninga", "ninja" ]
print(completeString(n,A))
  
