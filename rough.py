import string
import random

letters = list(string.ascii_lowercase)
random.shuffle(letters)

numbers = [str(n) for n in range(0,10)]
random.shuffle(numbers)

symbols = ["!", "@", "#","%"]

number_of_letters = random.randint(5,8)
number_of_numbers = random.randint(3,8)
number_of_symbols = random.randint(0,3)

random_letters = [letters[n] for n in range(0, number_of_letters + 1) ]
print(random_letters)

random_numbers = [numbers[n] for n in range(0, number_of_numbers + 1)]
print(random_numbers)

random_symbols = [symbols[n] for n in range(0, number_of_symbols + 1)]
print(random_symbols)

password_list = random_numbers + random_symbols + random_letters
random.shuffle(password_list)
print(password_list)

password = ""
for n in password_list:
    password += n
print(password)
