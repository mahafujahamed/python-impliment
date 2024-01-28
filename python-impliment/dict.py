
thisdict = {
    "brand" : "Frod",
    "model" : "Mustang",
    "year" : 2020
}

print(thisdict)
print(thisdict["model"])

#  dict constructor
thisdict = dict(brand="Ford",model="Mustang",year=2020)
print(thisdict)
x = thisdict.keys()
print(x)
thisdict["name"] = "Mahafuj"
print(x)
thisdict.update({"color": "red"})
print(thisdict)
x = thisdict.values()
print(x)

mydict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2020
}
for x in mydict:
    print(x)
for x in mydict:
    print(mydict[x])

for x in mydict.values():
    print(x)

for x in mydict.keys():
    print(x)

for x, y in mydict.items():
    print(x, y)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break