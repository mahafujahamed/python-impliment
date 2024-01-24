thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

mylist = list(("apple", "banana", "cherry", "grap"))
print(mylist)
print(mylist[2])
# print the last item of the list
print(mylist[-1])

newlist = ["apple", "banana", "cherry", "grap", "orange", "kiwi", "melon", "mango"]
print(newlist[3:5])

if "apple" in newlist:
    print("apple", "is in the fruits list")

newlist = ["apple", "banana", "cherry", "grap", "orange", "kiwi", "melon", "mango"]
oldlist = ["tomato", "potato", "carrot", "onion"]
newlist.extend(oldlist)
print(newlist)
newlist[3] = "papya"
newlist.insert(2, "watermelon")
newlist.append("cocunut")
newlist.remove("bananaw") # remove item from the list
print(newlist)