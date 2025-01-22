#-----------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#-----------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#-----------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#-----------
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#-----------
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#-----------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#-----------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#-----------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#-----------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#-----------
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#-----------
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#-----------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#-----------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#-----------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#-----------
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#-----------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#-----------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#-----------
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#-----------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#-----------
tuple1 = ("abc", 34, True, 40, "male")

#-----------
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#-----------
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)