class Edureka:
  def __init__(self) -> None:
    self.course = "PYTHON OOPS Course"
    self.__tech = "Python"  # double underscore makes private

  def CourseName(self):
    return self.course + self.__tech
  
  def get_tech(self):
    return self.__tech

  def set_tech(self,t):
    self.__tech = t


ob = Edureka()

ob.set_tech("ML COURSE")
ob.get_tech

print(ob.course)
print(ob.CourseName())
print(ob._Edureka__tech)