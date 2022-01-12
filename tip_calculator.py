
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Welcome message
print("Welcome to the tip calculator")

# Enter the total bill amount
total_bill = input("What was the total bill? $")
# Enter tip percentage 
tip_percentage = input("What percentage tip would you like to give? ")
# Number of people splitting the bill
number_of_guests = input("How many people are splitting hte bill? ")

# Calculator of total payment per person
percetage_applied = 1 + float(tip_percentage) / 100
total_per_guest = (float(total_bill) * percetage_applied) / int(number_of_guests)
total_per_guest_rounded = round(total_per_guest, 2)

print(total_per_guest_rounded)
