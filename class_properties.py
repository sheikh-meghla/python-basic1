class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x = Person("Meghla", 17)

print(x.name)
print(x.age)

#

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Meghla")
p2 = Person("Liza")

Person.lastname = "Sheikh"

print(p1.lastname)
print(p2.lastname)