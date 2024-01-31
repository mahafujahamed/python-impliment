price = 50

txt = "I can take dinner in {} BDT only."
text = "I can take dinner in {: .2f} BDT only."

print(txt.format(price))

print(text.format(price))

name = input("What is your name? ")
print("Hi! " + name)