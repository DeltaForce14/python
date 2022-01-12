
# Password Generator 

from abc import abstractproperty
import random

print("Welcome to Password Generator!")

# choice of letters, symbols, numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Input
letters_input = input("How many letters would you like in your password? \n")
symbols_input = input("How many symbols would you like in your password? \n")
numbers_input = input("How many numbers would you like in your password? \n")

# Changing input to integers
letters_int = int(letters_input)
symbols_int = int(symbols_input)
numbers_int = int(numbers_input)
# Total length of the passwords
total_length = letters_int + symbols_int + numbers_int

password_list = []

# Adding andom letters to password list
for letter in range(0, letters_int):
    letter_choice = random.choice(letters)
    password_list.append(letter_choice)

# Adding random symbols to password list
for symbol in range(0, symbols_int):
    symbol_choice = random.choice(symbols)
    password_list.append(symbol_choice) 

# Adding random numners to password list
for number in range(0, symbols_int):
    number_choice = random.choice(numbers)
    password_list.append(number_choice)

# Randomly shuffling elements in the password list. Needs to be shuffled in original list
random.shuffle(password_list)
# Join elemenets in the list
password = ""
for char in password_list:
    password += char

print(f"This is your password: {password}")    





 