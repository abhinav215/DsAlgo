class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    self.isEnd = False
    #dictionary with key as character and value as node
    self.child={}
      

#   def insertAndCounting(self, word: str) -> None:
#     flag=0
#     currentNode = self
#     for ele in word:
#       if ele not in currentNode.child:
#         currentNode.child[ele] = Trie(ele)
#       currentNode=currentNode.child[ele]
#     if currentNode.isEnd:
#       return 0
#     currentNode.isEnd = True
#     return 1
    

# def countDistinctSubstrings(s):
#   trie = Trie()
#   n =len(s)
#   ans = 0
#   for i in range(n):
#     for j in range(i,n+1,1):
#       ans += trie.insertAndCounting(s[i:j])
#       print(s[i:j],ans)
#   return ans

#Above comment kia hua code O(N^3) time complexity hai



def countDistinctSubstrings(s):
  trie = Trie()
  n =len(s)
  count = 0
  for i in range(n):
    currentNode = trie
    for j in range(i,n):
      print(s[j])
      if s[j] not in currentNode.child:
        count+=1
        currentNode.child[s[j]] = Trie(s[j])
        currentNode = currentNode.child[s[j]]
        currentNode.isEnd = True
      else:
        currentNode = currentNode.child[s[j]]
    if not currentNode:
      currentNode=True
      count+=1
  print(count+1)
  return count+1



# O(N^2)




# s = "abab"
s = "sds"
print(countDistinctSubstrings(s))
  