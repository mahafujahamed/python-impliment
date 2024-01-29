x = lambda a : a - 51
print(x(100))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)

print(mydoubler(20))