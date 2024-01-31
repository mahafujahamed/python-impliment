class Person:
    def __init__(self, fname, lname):
        self.fastname = fname
        self.lastname = lname

    def printname(self):
        print(self.fastname, self.lastname)
x = Person("Developer", "Mahafuj")
x.printname()

class Student(Person):
    pass
x = Student("Developer", "Mahafuj")
x.printname()

class Student1(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student1("Developer", "Mahafuj")
x.printname()

class Student2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student2("Developer", "Mahafuj")
x.printname()


class Student3(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student3("Developer", "Mahafuj", 2019)
print(x.graduationyear)


class student4(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.fastname, self.lastname, "to the class of", self.graduationyear)

x = student4("Developer", "Mahafuj", 2019)
x.welcome()