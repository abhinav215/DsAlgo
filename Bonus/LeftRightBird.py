#Bird should not face each other
#l means face left 
#r means face right

class Node:
  def __init__(self,char,count) -> None:
      self.count = count
      self.char = char


def answer(s):
  sta= []
  for ele in s:
    if sta==[]:
      sta.append(Node(ele,1))
    elif sta[-1].char!=ele:
      # print(sta[-1].char,ele)
      sta.append(Node(ele,1))
    elif sta[-1].char==ele:
      sta[-1].count+=1

  item=""
  number=""
  for i in range(len(sta)):
    item+=sta[i].char+"\t"
    number+=str(sta[i].count)+"\t"
  print(item)
  print(number)

  start=0
  end= len(sta)-1
  ans= 0
  while start<end:
    if sta[start].char == "l":
      start+=1
    if sta[end].char == "r":
      end-=1
    if sta[start].char == "r" and sta[end].char == "l":
      if sta[start].count<sta[end].count:
        ans+=sta[start].count
        print(sta[start].char,sta[end].char,ans)
        start+=1
      if sta[start].count>=sta[end].count and start!=end:
        ans+=sta[end].count
        print(sta[start].char,sta[end].char,ans)
        end-=1
    
  print(ans)



s = "lllrlrrllr"
s = "lllrlrrrllllr"
s = "rlrlrl"
answer(s)