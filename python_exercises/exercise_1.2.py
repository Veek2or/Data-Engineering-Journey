'''
1.2 Comprehensions. Rewrite each loop from 1.1 as a comprehension where it reads more clearly. 
In your log, name one place where a comprehension made it worse, and why.
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
#Method 1 - using list comprehension for the inner loop only
student_names = ["Alice", "Ben","Chloe","Daniel","Emma"]

for student_name in student_names:
    marks = [mark for student, _, mark in results if student == student_name]
    average = sum(marks)/len(marks)
    print("Average mark of " + str(student_name) + " :" +  str(average))

#Method 2 - using dictionary comprehension
averages = {
    student_name: (
        sum([mark for student, _, mark in results if student == student_name])
        / len([mark for student, _, mark in results if student == student_name])
    ) 
    for student_name in student_names
    }
print(averages)

#Log: Although method 2 produces a simpler output, personally method 1 is much simpler to follow
#Method 2 feels like a one long run-on sentence and there are too many brackets

'''
Part 2
'''
modules = ["Python", "SQL", "Statistics", "Data Modelling"]

#List comprehension used for inner loop whith a normal outer loop
module_average = []
for m in modules:
    module_marks = [mark for _, module, mark in results if module == m]
    average = sum(module_marks)/len(module_marks)
    module_average.append(average)

position = module_average.index(max(module_average))
highest_module_name = modules[position]

print("Highest average module: " + str(highest_module_name) + " " + str(max(module_average)) + " points")

'''
Part 3
'''
#List comprehension used in place of a for loop
failed = {student for student, _, mark in results if mark < 40}
print(failed)

#Log summary: Overall list comprehension can achieve the same thing for loop does with less lines of code (most of the time).