class Person:
  def __init__(self, name, email):
    self.name = name
    self.__email = email  

p1 = Person("meghla", "meghla@gmail.com")
print(p1.name)
print(p1.__email)

#

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary 

p1 = Person("Meghla", 50000)
print(p1.name)
print(p1._salary)