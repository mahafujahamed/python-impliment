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
newlist.remove("banana") # remove item from the list
print(newlist)
newlist.pop() # remove the last item from the list
print(newlist)

thislist =  ["apple", "banana", "cherry", "grap", "orange", "kiwi", "melon", "mango"]

del thislist[-1]
print(thislist)

for x in thislist:
    print(x)

listmaker = ["fruit", "valuable", "vegetable"]
i = 0
while i < len(listmaker):
    print(listmaker[i])
    i = i + 1

thislist =  ["apple", "banana", "cherry", "grap", "orange", "kiwi", "melon", "mango"]
thislist.sort()
print(thislist)
listup = []

for x in thislist:
    if "a" in x:
        listup.append(x)

print(thislist)
print(listup) 
newlist = [x for x in thislist if x != "apple"]
print(newlist)      

listitem = [x for x in range(10)]
print(listitem)
listitem = [x for x in range(10) if x < 5]
newlist = ['mahafuj' for x in range(10)]
print(newlist)
print(listitem)