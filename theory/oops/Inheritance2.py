class A:
  def __init__(self) -> None:
    print("A ka init")
  def lol1(self):
    print("CLass A ka func")


class B(A): 
  def __init__(self) -> None:
    super().__init__()   #to use parent(super class) method
    print("B ka init")
  def lol2(self):
    print("CLass B ka func")

b = B()
