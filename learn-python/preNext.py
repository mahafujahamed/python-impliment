a = int(input("Enter a number: "))
nextNumber = a + 1
previousNumber = a - 1
nextTest = "The next number for the number {a} is {nextNumber}"
preTest = "The previous number for the number {a} is {previousNumber}"
print(nextTest.format(a = a, nextNumber = nextNumber))
print(preTest.format(a = a, previousNumber = previousNumber))
