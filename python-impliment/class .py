class myclass:
    x = "Developer Mahafuj"

c = myclass()
print(c.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Mahafuj", 24)
print(p1.name)
print(p1.age)

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p2 = Person1("Mahafuj", 24)
print(p2)

class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = test("Mahafuj", 25)
p1.myfunc()

class test1:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(abc):
        print("Hello my friend " + abc.name + str(abc.age))

p3 = test1("Sourov", 23)
p3.myFunc()