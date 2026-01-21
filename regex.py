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
