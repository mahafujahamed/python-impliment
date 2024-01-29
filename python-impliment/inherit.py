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
