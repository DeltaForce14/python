
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print("Welsome to Love Calculator!")

first_name = input("What is your full name? ").lower()
second_name = input("What is your crush's full name? ").lower()

names_combined = first_name + second_name

true_count = names_combined.count("t") + names_combined.count("r") + names_combined.count("u") + names_combined.count("e") 
love_count = names_combined.count("l") + names_combined.count("o") + names_combined.count("v") + names_combined.count("e") 


result = (str(true_count)+str(love_count))
result_int = int(result)



if (result_int < 10) or (result_int > 90):
    print(f"You score is {result}. You go together like coke and mentos.")
elif (result >= 40) and (result <= 50):
    print(f"Your result is {result}. You are alright together.")
else:
    print(f"Your score is {result}")    