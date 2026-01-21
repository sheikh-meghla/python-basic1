import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

  #

txt = "The rain in Spain"
x = re.findall("r", txt)
print(x)

#

txt = "The rain in Spain"
x = re.search("\s", txt)

print("Hello:", x.start()) 

#

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#

txt = "The rain in Spain"
x = re.sub("\s", "2", txt)
print(x)

#

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())