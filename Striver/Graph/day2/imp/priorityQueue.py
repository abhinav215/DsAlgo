from queue import PriorityQueue


#here the priority of ele is element themself
def answer():
  qu = PriorityQueue()
  qu.put(1)   #log(n) put
  qu.put(11)
  qu.put(21)
  qu.put(1111)
  qu.put(14)
  qu.put(51)
  qu.put(122)
  qu.put(18)
  print(qu)
  for ele in qu:
    print(ele)
  # for i in range(8):
  #   print(qu.get())

# answer()

# A typical pattern for entries is a tuple in the form: (priority_number, data).

def answer2():
  qu = PriorityQueue()
  qu.put((1,"hello"))   #log(n) put
  qu.put((11,"jh"))
  qu.put((21,"kj"))
  qu.put((1111,"po"))
  qu.put((14,"yf"))
  qu.put((51,"rd"))
  qu.put((122,"hgs"))
  qu.put((18,"dwsd"))
  print(qu)
  for i in range(8):
    print(qu.get()[1])
  print(qu.empty())


answer2()


# function
# get,put,empty
