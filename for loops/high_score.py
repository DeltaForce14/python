# Program that calculates the highest score from a List of scores

student_scores = input("Input a list of student scores ").split()

# change input type to integer
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


highest_score = 0 
for n in student_scores:
    if highest_score < n:
        highest_score = n

print(f"The highest score in the class is: {highest_score}")

