# message string to be used for each student
names = input("Enter name separated by comma: ").title().replace(" ", "").split(",") # get and process input for a list of names
assignments = input("Enter assignment counts separated by comma: ").replace(" ", "").split(",") # get and process input for a list of the number of assignments
grades = input("Enter grades separated by comma: ").replace(" ", "").split(",")# get and process input for a list of grades

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print("\nHi {},\n\nThis is a reminder that you have {} assignments left to \n"
          "submit before you can graduate. You're current grade is {} and can increase \n"
          "to {} if you submit all assignments before the due date.\n".format(name, assignment, grade, int(grade) + int(assignment)*2))



