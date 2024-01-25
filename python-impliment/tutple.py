x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "Mahafuj"
x = tuple(y)
print(x)
z = ("orange",)
x += z
print(x)

# unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# unpacking a tuple