import inflect

def number_to_word(number):
    p = inflect.engine()
    return p.number_to_words(number)

input_number = int(input("Enter a number: "))
words = number_to_word(input_number)
print(f"{input_number} in words is {words}")