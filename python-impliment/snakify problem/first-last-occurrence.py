a = input("") # input string
if a.count("f") == 1: # if the count of "f" is equal to 1
    print(a.index("f")) # print the index of "f"
elif a.count("f") >= 2: # if the count of "f" is greater than or equal to 2
    print(a.index("f"), a.rindex("f")) # print the index of "f" and the last index of "f"
else: # if the count of "f" is less than 1
    pass # do nothing


