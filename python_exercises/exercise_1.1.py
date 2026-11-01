'''
1.1 Marks analyser. Type a list of 20 tuples yourself: 
(student, module, mark) with 5 students and 4 modules. 
Without importing anything, compute: each student's average; 
the module with the highest average; every student who failed any module (under 40).
 Done when: your output matches numbers you worked out by hand.
'''
#A list storing 20 tuples (5 students, 4 subjects)
results = [
    ("Alice", "Python", 78),
    ("Alice", "SQL", 85),
    ("Alice", "Statistics", 62),
    ("Alice", "Data Modelling", 71),
    ("Ben", "Python", 54),
    ("Ben", "SQL", 67),
    ("Ben", "Statistics", 73),
    ("Ben", "Data Modelling", 58),
    ("Chloe", "Python", 91),
    ("Chloe", "SQL", 88),
    ("Chloe", "Statistics", 79),
    ("Chloe", "Data Modelling", 84),
    ("Daniel", "Python", 45),
    ("Daniel", "SQL", 52),
    ("Daniel", "Statistics", 38),
    ("Daniel", "Data Modelling", 61),
    ("Emma", "Python", 69),
    ("Emma", "SQL", 74),
    ("Emma", "Statistics", 81),
    ("Emma", "Data Modelling", 66),
]

'''
Part 1
'''
#List of student names
student_names = ["Alice","Ben","Chloe","Daniel","Emma"]

#Loop for finding the average marks of each student
for student_name in student_names:
    #empty variable to add total marks
    total = 0
    #empty variable to keep track of count
    count = 0
    for student, module, mark in results:
        if student == student_name:
            total = total + mark
            count += 1
    average = total/count
    print("Average mark of " + str(student_name) + " :" + str(average))

'''
Part 2
'''
#List of modules
modules = ["Python", "SQL", "Statistics", "Data Modelling"]

#Empty list to store average module marks
module_average = []

#Loop for finding the highest average module
for m in modules:
    total = 0
    count = 0
    for student, module, mark in results:
        if module == m:
            total = total + mark
            count += 1
    average = total/count
    module_average.append(average)

#Print to check list
print(module_average)

#Find the highest score
highest_module_average = max(module_average)

#Find the index of the highest score
position = module_average.index(highest_module_average)

#Use the index to find the name of the module
highest_module_name = modules[position]

#Print to check module name
print(highest_module_name)
print("Highest average module: " + str(highest_module_name) + " " + str(highest_module_average) + " points")

'''
Part 3
'''
#Empty list to store students who failed any module
failed = []

for student, module, mark in results:
        if mark < 40 and student not in failed:
            failed.append(student)
print(failed)

