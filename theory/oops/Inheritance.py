class A:
  def lol1(self):
    print("CLass A ka func")

class C:
  def lol3(self):
    print("CLass C ka func")


class B(A,C): #B(A) mean B inherit A
  def lol2(self):
    print("CLass B ka func")



a = A()
a.lol1()
print("============")
b = B()
b.lol2()
b.lol1()
b.lol3()