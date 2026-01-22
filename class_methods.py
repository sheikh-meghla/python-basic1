class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Meghla")
p1.greet()

#

class Calculator:
  def sum(self, a, b):
    return a + b

  def mult(self, a, b):
    return a * b

calc = Calculator()
print(calc.sum(3, 2))
print(calc.mult(3, 2))


#

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Meghla", 17)
p1.celebrate_birthday()
p1.celebrate_birthday()

