#  creating a function
 
def myFunction():
    print("Hey! I am here .......")

myFunction()

def my_function(name):
    print(name + " Ahamed")

my_function("Mahafuj")
my_function("habib")

def function(food):
    for x in food:
        print(x)

food = ["apple", "banana", "cherry"]
function(food)

# only specific argument
def myFunction(x, /):
    print(x)

myFunction(6)