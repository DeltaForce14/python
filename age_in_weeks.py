
# How many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age?")

years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

