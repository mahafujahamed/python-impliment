# this task should not use loops and if statements
a = input("")
b = (a[0:len(a) // 2]) # first half
c = (a[len(a) // 2:]) # second half
print(c, b, sep = " ") # second half + first half
# 2nd solution
# a = input("")
# print(a[len(a) // 2:] + a[:len(a) // 2]) # second half + first half
# 3rd solution
# a = input("")
# print(a[len(a) // 2:] + " " + a[:len(a) // 2]) # second half + first half
# 4th solution
# a = input("")
# print(a[len(a) // 2:] + " " + a[:len(a) // 2]) # second half + first half
