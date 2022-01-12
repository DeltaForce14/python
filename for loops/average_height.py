
# Calculates the average student height from a List of heights. 

student_heights = input("Input a list of student heights ").split()
total = 0
number_of_items = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  

for height in student_heights:
    total += height
    number_of_items += 1

average = round(total / number_of_items, 2)

print(average)

  

