x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
if x < y and x < z:
    print(x)
elif y < x and y < z:
    print(y)
else:
    print(z)
