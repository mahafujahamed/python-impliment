name = input("Enter your name: ")
print(name[2]) # 3rd character
print(name[-2]) # 2nd last character
print(name[0:5]) # first 5 characters
print(name[0:len(name) - 2]) # all characters
print(name[0:len(name):2]) # every 2nd character
print(name[1:len(name):2]) # every 2nd character starting from 2nd character
print(name[::-1]) # reverse the string
print(name[::-2]) # reverse the string and every 2nd character
print(len(name)) # length of the string
# print(name[100]) # IndexError: string index out of range