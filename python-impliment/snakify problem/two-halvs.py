a = input("")
b = (a[0:len(a) // 2]) # first half
c = (a[len(a) // 2:]) # second half

print(c + b) # second half + first half
