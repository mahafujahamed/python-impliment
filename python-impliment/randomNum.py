import random
print(random.randrange(1, 10))

# multiline string
a = """lorem30
ipsum lorem30
ipsum lorem30
ipsum lorem30
ipsum lorem30
    ipsum lorem30 """ 
print(a)
print(a[11])

for x in "Mahafuj":
    print(x)

txt = "The best things in life are free!"
print("out " not in txt)

txt="i am developer Mahafuj"
print(txt.upper())
if "mahafuj" in txt:
    print("Yes, Mahafuj is present")


a = " Man is mortal !"
print(a.split(" "))
print(a.strip())
print(a.replace("Man", "Human"))

age = 25
text = "My name is Mahafuj Ahamed, and I am {}"
print (text.format(age))

text = "Hello! Friend, \"How\" are you?"
print(text)

octal = "\110\30\154\47\100"
print(octal)

# Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)