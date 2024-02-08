a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)