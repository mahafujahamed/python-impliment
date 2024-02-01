name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + " likes " + favorite_color)

#  birth year calculating age
birth_year = input("Birth year: ")
age = 2024 - int(birth_year)
print(age)

# weight in pounds to kilograms

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Strings formating

first = 'Mahafuj'
last = 'Ahamed'
message = first + ' [' + last + '] is a Developer'
msg = f'{first} [{last}] is a Developer'
print(message)
print(msg)

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
    
else:
    down_payment = price * 0.2

print(f"Down payment: {down_payment}")

