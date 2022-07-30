


x = 4
y = 5

print(x+y)


a =4
b = 5
print(int.__add__(a,b))



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Student:
  def __init__(self,m1,m2) -> None:
    self.m1 = m1
    self.m2 = m2

  def __add__(self,other):
    m1 = self.m1+other.m1
    m2 = self.m2+other.m2
    s3 = Student(m1,m2)
    return s3


s1 = Student(11,66)
s2 = Student(76,49)
ans = s1+s2
print(ans,ans.m1,ans.m2)