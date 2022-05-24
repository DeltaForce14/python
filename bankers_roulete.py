
#Choose random name to pay the bill

import random

#Input: list of names
names_string = input("Give me everybody's names, separated by a comma. ")

#Split names into the list 
names = names_string.split(", ")


# List with index number of items form list 'names'
index_list = []
for n in range(0, len(names)):
    index_list.append(n)

# Choose random number from the index list 
random_number = random.choice(index_list)
   
#Print name using random choice 
print(names[random_number])



