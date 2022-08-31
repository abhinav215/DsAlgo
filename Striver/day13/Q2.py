class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.arr = []
        self.frontPointer =0
        self.rear=0


    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        if self.rear == 0:
            return True
        return False



    def enqueue(self, data) :
        self.arr.append(data)
        self.rear+=1
        self.count  +=1



    def dequeue(self) :
        if self.rear == 0:
            return -1
        self.rear -=1
        ans = self.arr[self.frontPointer]
        self.arr[self.frontPointer] = -1
        self.frontPointer +=1
        return ans



    def front(self) :
        if self.rear == 0:
            return -1
        return self.arr[self.frontPointer]
        