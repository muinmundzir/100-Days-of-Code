# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# selected_letters_list = []
selected_letters = ''
for letter in range(0, nr_letters):
    random_number = random.randint(0, len(letters) - 1)
    selected_letters += letters[random_number]

selected_symbols = ''
for symbol in range(0, nr_symbols):
    random_number = random.randint(0, len(symbols) - 1)
    selected_symbols += symbols[random_number]

selected_numbers = ''
for number in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    selected_numbers += numbers[random_number]

password = selected_letters + selected_symbols + selected_numbers
print(
    f"Here is your password: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = ''.join(random.sample(password, len(password)))

print(
    f"Here is your more random password: {password_hard}")
