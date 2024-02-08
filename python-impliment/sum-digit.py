num = int(input("Enter three integer number: "))
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
print(f"The sum of the digits is {sum}.")