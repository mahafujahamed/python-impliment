hours = int(input("Enter the hour: "))
minutes = int(input("Enter the min: "))
seconds = int(input("Enter the sec: "))
firstTimeStamp = hours * 3600 + minutes * 60 + seconds
hours = int(input("Enter the hour: "))
minutes = int(input("Enter the min: "))
seconds = int(input("Enter the sec: "))
secondTimeStamp = hours * 3600 + minutes * 60 + seconds
print(secondTimeStamp - firstTimeStamp)