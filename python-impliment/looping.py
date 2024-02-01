# x = 1
# for x in range(1,26):
#     print(x)
#     x += 1
# print("o------------o------------o")

# i = 1

# while i <= 6:
#     print('*' * i)
#     i += 1
# print("Wow!")

# largest number in a list

numbers = [5, 32, 56, 4, 5, 6, 20]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)