class Node:
    def __init__(self,data=None,next = None,pre = None):
        self.data = data
        self.next = next
        self.pre = pre

    
    def removeNode(self):
        previous = self.pre  
        nex = self.next
        nex.pre = previous
        previous.next = nex

class DoubleLinkList:
    def __init__(self):
        self.head= Node("Head",None,None)
        self.tail= Node("Tail",None,self.head)
        self.head.next = self.tail

    def insert(self,data):
        start = self.head
        nex = self.head.next
        adding = Node(data,nex,start)
        start.next = adding
        nex.pre = adding
        return adding
      

    def printingNext(self):
        tvr = self.head
        ans = ""
        while tvr:
            ans += str(tvr.data) + "->"
            tvr = tvr.next
        print(ans)

    def printingPre(self):
        tvr = self.tail
        ans = ""
        while tvr:
            ans += str(tvr.data) + "->"
            tvr = tvr.pre
        print(ans)
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic={}
        self.doubleLt = DoubleLinkList()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        add = self.dic[key]
        val = add.data[1]
        add.removeNode()
        add = self.doubleLt.insert([key,val])
        self.dic[key]= add
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            add = self.dic[key]
            add.removeNode()
            nodeadd = self.doubleLt.insert([key,value])
            self.dic[key] = nodeadd
            return
        if len(self.dic)==self.capacity:
            add= self.doubleLt.tail.pre.pre
            k = add.next.data[0]
            add.next = self.doubleLt.tail
            self.doubleLt.tail.pre = add
            #remove from dict
            print(k)
            self.dic.pop(k)
        add = self.doubleLt.insert([key,value])
        self.dic[key]=add
            
        
        
        
        # if key in self.dic and self.dic[key]!=-1:
        #     self.rear+=1
        # self.rear+=1
        # if self.rear - self.front > self.capacity:
        #     self.dic[self.arr[self.front]] = -1
        #     self.front+=1
        # self.arr.append(key)
        # self.dic[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

abc =  LRUCache(2)
abc.put(1, 1)
abc.put(2, 2)
print(abc.get(1))
abc.put(3, 3)
print(abc.get(2))
abc.put(4, 4)
print(abc.get(1))
print(abc.get(3))
print(abc.get(4))
