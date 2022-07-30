class Laptop:
  def code(self,ide):
    ide.execute()


class Pycharm:
  def execute(self):
    print("Pycharm")

class VSCode:
  def execute(self):
    print("VScode")


# ide = Pycharm()
# l = Laptop()
# l.code(ide)


ide = VSCode()
l = Laptop()
l.code(ide)

# it doesnt matter what is the class of ide ... pycharm or VScode ... the only catch is it should have execute funct in it