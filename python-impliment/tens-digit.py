number = int(input("Enter an integer number: "))
tens_digit = (number // 10) % 10
print(f"The tens digit of {number} is {tens_digit}.")
# Output:
# Enter an integer number: 123456
# The tens digit of 123456 is 5.
# Enter an integer number: 123456789
# The tens digit of 123456789 is 8.
# Enter an integer number: 1234567890
# The tens digit of 1234567890 is 9.
# Enter an integer number: 12345678901
# The tens digit of 12345678901 is 0.
# Enter an integer number: 123456789012
# The tens digit of 123456789012 is 1.
# Enter an integer number: 1234567890123
# The tens digit of 1234567890123 is 2.
# Enter an integer number: 12345678901234
# The tens digit of 12345678901234 is 3.
# Enter an integer number: 123456789012345
# The tens digit of 123456789012345 is 4.
# Enter an integer number: 1234567890123456
# The tens digit of 1234567890123456 is 5.