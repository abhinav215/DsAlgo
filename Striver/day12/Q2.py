class Trie:
    def __init__(self,st=None):
        self.character = st
        self.startCount = 0
        self.endCount = 0
        self.child = {}

    def insert(self, word):
        currentNode = self
        for ele in word:
            if ele not in currentNode.child:
                currentNode.child[ele]=Trie(ele)
            currentNode.startCount +=1
            currentNode = currentNode.child[ele]
        currentNode.startCount +=1
        currentNode.endCount+=1
            
    def countWordsEqualTo(self, word):
        currentNode = self
        for ele in word:
            if ele not in currentNode.child:
                return 0
            currentNode = currentNode.child[ele]
        return currentNode.endCount

    def countWordsStartingWith(self, word):
        currentNode = self
        for ele in word:
            if ele not in currentNode.child:
                return 0
            currentNode = currentNode.child[ele]
        return currentNode.startCount

    def erase(self, word):
        currentNode =self
        for ele in word:
            if ele not in currentNode.child:
                return
            currentNode = currentNode.child[ele]
            currentNode.startCount -=1
        currentNode.endCount -= 1