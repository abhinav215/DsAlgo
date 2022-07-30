class Node:
  def __init__(self,char,count) -> None:
      self.count = count
      self.char = char



def answer(s,k):
  sta= []
  for ele in s:
    if sta==[]:
      sta.append(Node(ele,1))
    elif sta[-1].char!=ele:
      # print(sta[-1].char,ele)
      sta.append(Node(ele,1))
    elif sta[-1].char==ele:
      sta[-1].count+=1
      if sta[-1].count==k:
        sta.pop()
  out = ""
  for i in range(len(sta)):
    out+=sta[i].char*sta[i].count
  return out


s = "aabbcccbaa"
k=3
out="a"
print(answer(s,k))