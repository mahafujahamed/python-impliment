class Library:
    def __init__(self,author,title):
        self.author = author
        self.title = title

    def setAuthor(self,author):
        self.author = author

    def setTitle(self,title):
        self.title = title

    def getAuthor(self):
        return self.author
    
    def getTitle(self):
        return self.title
    
book1=Library("MAhfuz","Python")
book2=Library("Ahmed","Python1")

print("Book1: "+book1.getTitle()+" Author name: "+book1.getAuthor())
print("Book2: "+book2.getTitle()+" Author name:  "+book2.getAuthor())

book1.setTitle("Python3")
book2.setTitle("Java")

print("Book1: "+book1.getTitle()+" Author name: "+book1.getAuthor())
print("Book2: "+book2.getTitle()+" Author name:  "+book2.getAuthor())
