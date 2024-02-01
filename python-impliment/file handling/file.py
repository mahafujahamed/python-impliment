# f = open("text.txt", "x")
# f = open("text.txt", "a")
# f.write("Hello World")
# f.close()

# f = open("text.txt", "r")
# print(f.read(5))

import os
if os.path.exists("text.txt"):
    os.remove("text.txt")

else:
    print("The file does not exist")

os.rmdir("text.txt")