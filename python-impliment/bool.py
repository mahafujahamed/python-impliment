print(10==3)
print(10!=3)
print(10>3)
print(10<3)
print(10>=3)
print(10<=3)
print(10==3 and 10==3)  
print(10==3 or 10==3)

a = 300
b = 500

if a > b:
    print("a is not greater than b")
else:
    print("b is greater than a")

print(bool(30))

class myClass():
    def __len__(self):
        return 0
    
myObj = myClass()
print(bool(myObj))

def myFunction():
    return True
print(myFunction())

def myFunction():
    return False 

if myFunction():
    print("YES!")
else:
    print("NO!")    