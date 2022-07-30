from abc import ABC,abstractclassmethod

class Computer(ABC):
  @abstractclassmethod
  def process(self):
    pass

# class Laptop(Computer):
#   pass

# comp = Computer()
# Error bcZ emply class hai



# Comp1 = Laptop()
# Laptop.process()
# Error bcz abhi bhi class emply hai


class Laptop(Computer):
  def process(self):
    print("running")

comp1 = Laptop()
comp1.process()