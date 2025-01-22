#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#-----------
print(len(thisdict))
#-----------
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#-----------
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#-----------
x = thisdict.get("model")
print(x)
#-----------
x = thisdict.keys()
print(x)
#-----------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#-----------
x = thisdict.values()
print(x)
#-----------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#-----------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#-----------
x = thisdict.items()
print(x)
#-----------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#-----------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])
#-----------
for x in thisdict.values():
  print(x)
#-----------
for x in thisdict.keys():
  print(x)
#-----------
for x, y in thisdict.items():
  print(x, y)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#-----------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#-----------
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#-----------
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#-----------
print(myfamily["child2"]["name"])
#-----------
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#-----------
a = 33
b = 200
if b > a:
  print("b is greater than a")
#-----------
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#-----------
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#-----------
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#-----------
if a > b: print("a is greater than b")
#-----------
a = 2
b = 330
print("A") if a > b else print("B")
#-----------
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#-----------
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#-----------
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#-----------
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#-----------
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#-----------
a = 33
b = 200

if b > a:
  pass
#-----------
i = 1
while i < 6:
  print(i)
  i += 1

#-----------
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#-----------
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#-----------
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#-----------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#-----------
for x in "banana":
  print(x)
#-----------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#-----------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#-----------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#-----------
for x in range(6):
  print(x)
#-----------
for x in range(2, 6):
  print(x)
#-----------
for x in range(2, 30, 3):
  print(x)
#-----------
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#-----------
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#-----------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#-----------
for x in [0, 1, 2]:
  pass
#-----------

