
# Select a random name from a list of names. The person selected will have to pay 
# for everybody's food bill.

import random

names = input("Input names separated by coma: ")
names_list = names.split(",")
lenght_list = len(names_list)

random_choice = (random.randint(0, lenght_list-1))

chosen_person = names_list[random_choice]

print(chosen_person)


