#-----------
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#-----------
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#-----------
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#-----------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#-----------
thislist = ["apple", "banana", "cherry"]
del thislist
#-----------
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#-----------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#-----------
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#-----------
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#-----------
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#-----------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#-----------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#-----------
newlist = [x for x in fruits if x != "apple"]
#-----------
newlist = [x for x in fruits]
#-----------
newlist = [x for x in range(10)]
#-----------
newlist = [x for x in range(10) if x < 5]
#-----------
newlist = [x.upper() for x in fruits]
#-----------
newlist = ['hello' for x in fruits]
#-----------
newlist = [x if x != "banana" else "orange" for x in fruits]