a = int(input("First Group Members: "))
b = int(input("Second Group Members: "))
c = int(input("Third Group Members: "))
totalDesk = int(a / 2 + b / 2 + c / 2) + (a % 2 + b % 2 + c % 2)
print(totalDesk)