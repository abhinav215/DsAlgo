class Trie:
    def __init__(self,character="root"):
        self.ch=character
        self.count =0
        self.isEnd = False
        self.dic = {}


def printint(tr):
    print(tr.dic)


def longestCommonPrefix( strs) -> str:
    tr = Trie()
    n= len(strs)
    for ele in strs:
        root = tr
        for letter in ele:
            if letter not in root.dic:
                root.dic[letter] = Trie(letter)
                print(root.dic)
            root = root.dic[letter]
            root.count+=1
        root.isEnd = True
    count = 0
    word = strs[0]
    ans = ""
    count=0
    root = tr
    for letter in word:
        if count> root.count:
            break
        if root.isEnd==True:
            break
        count = root.count
        root = root.dic[letter]
        ans+=letter
    print(root.count,ans)
    return ans



strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
longestCommonPrefix(strs)