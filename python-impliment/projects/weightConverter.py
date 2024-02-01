print("-------converte into kilos or pounds-------")

weight = int(input("Weight: "))
unit = input("(l)bs or (k)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")