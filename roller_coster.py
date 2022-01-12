
# Find out if year is a leap year
height = int(input("What is your heigh? "))
age = int(input("What is your age? "))
photo = input("Would you like photo? yes/no ")

if height >= 120:
    if age < 12:
        if photo == "yes":
            price = 5 + 3
        else: price = 5
    elif age <= 18:
        if photo == "yes":
            price = 7 + 3
        else: price = 7
    elif age >= 45 and age <= 55:
        price = 0  
        if photo == "yes":
            price = 3  
    elif photo == "yes":
        price = 10 + 3
    else: 
        price = 10  
else:
    print("You can't ride.")       

print(price)