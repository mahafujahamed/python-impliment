cube = int(input("Enter cube: "))
cubes = 0
for i in range(1, cube + 1):
    cubes += i ** 3
print(cubes)