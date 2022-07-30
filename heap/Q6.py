import collections


def topKFrequent( nums, k: int) :
    counter=collections.Counter(nums)
    print(counter)
    l=sorted(counter.items(),key=lambda x:x[1],reverse=True)
    print(l)
    print(i[0] for i in l[:k])
    return [i[0] for i in l[:k]]



nums = [1,1,1,2,2,3]
topKFrequent(nums,2)