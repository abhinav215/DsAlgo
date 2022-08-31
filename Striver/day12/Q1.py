class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    self.isEnd = False
    self.count = 0
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
    currentNode.count += 1


  def search(self, word: str) -> bool:
    currentNode = self
    for ele in word:
      if ele in currentNode.child:
        currentNode = currentNode.child[ele]
      else:
        return False
    if currentNode.isEnd:
      return True
    return False

  def startsWith(self, word: str) -> bool:
    currentNode = self
    for ele in word:
      if ele in currentNode.child:
        currentNode = currentNode.child[ele]
      else:
        return False
    return True




  def printing(self):
    currentNode = self
    st = ""
    for ele in currentNode.child:
      currentNode.child[ele].recursion(st)
      print("")

  def recursion(self,st):
    st+=self.character
    if self.count!=0:
      print(st,self.count)
    for ele in self.child:
      self.child[ele].recursion(st)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("char")
obj.insert("chari")
obj.insert("char")
obj.insert("chhari")
obj.insert("cchar")
obj.insert("schari")
obj.insert("charr")
obj.insert("chari")
obj.printing()
param_2 = obj.search("chari")
print(param_2)
# param_3 = obj.startsWith(prefix)