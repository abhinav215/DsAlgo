class Pen:
  def __init__(self,color,typeofInk) -> None:
    self.color = color
    self.type = typeofInk #get/ball

  def write(self):
    print("write")

  def intro(self):
    print(self.color,self.type)


pen1 = Pen("pink","gel")
pen1.write()
pen1.intro()