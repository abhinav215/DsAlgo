class A:
  def __init__(self) -> None:
    print("A ka init")
  def lol1(self):
    print("CLass A ka func")


class B: 
  def __init__(self) -> None:
    super().__init__()   #to use parent(super class) method
    print("B ka init")
  def lol2(self):
    print("CLass B ka func")



class C(A,B): 
  def __init__(self) -> None:
    super().__init__()   #MRO(Method Resolution Order) => left to right
    print("C ka init")
  def lol3(self):
    print("CLass C ka func")

b = C()
