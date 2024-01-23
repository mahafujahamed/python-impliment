# string type data
name = " Mahafuj Ahamed"
print(name)
print(type(name))
name1 = "Mahafuuj"
name2 = "Ahamed"
print("My full name is: ", name1 + " " + name2)

if 5 > 2:
    print("Five is greater than two!")

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
# creating a variable outside of a function, and use it inside the function
name = "Mahafuj Ahamed"

def myName():
    print("My name is: ", name)

myName()

# global variable
def myFunc():
    global x
x = "awesome"

myFunc()
print("Python is " + x)

complex = 2j
print(type(complex))

x = range(6)
print(x)

x = memoryview(bytes(5))
print(x)

x = frozenset({"apple", "banana", "cherry"})
print(x)

z = 3
c = complex(z)
print(c)