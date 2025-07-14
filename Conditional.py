grade = input("Enter the grade of the student: ")
grade = int(grade)  # Convert input to integer for comparison

if (grade >= 90):
    if (grade >= 95):
        grade = "A+"
    else:
        grade = "A"
elif (grade >= 80 and grade < 90):
    if (grade >= 85):
        grade = "B+"
    else:
        grade = "B"
elif (grade >= 70 and grade < 80):
    if (grade >= 75):
        grade = "C+"
    else:   
        grade = "C"
else:
    grade = "D"

print("Grade of the student is: " + grade)
# This code checks the grade of a student and assigns a letter grade based on the score.