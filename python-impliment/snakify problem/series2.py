A = int(input("Enter a number: "))
B = int(input("Enter a number: "))

if A < B:
    for i in range(A, B + 1):
        print(i)
elif A >= B:
    for i in range(A, B - 1, -1):
        print(i)