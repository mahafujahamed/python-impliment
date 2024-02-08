# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))
# e = int(input("Enter a number: "))
# f = int(input("Enter a number: "))
# g = int(input("Enter a number: "))
# h = int(input("Enter a number: "))
# i = int(input("Enter a number: "))
# j = int(input("Enter a number: "))
# print(a + b + c + d + e + f + g + h + i + j)
#  short hand for the above code
res = 0
for i in range(10):
    res += int(input("Enter a number: "))
print(res)