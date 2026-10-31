'''
1.1 Marks analyser. Type a list of 20 tuples yourself: 
(student, module, mark) with 5 students and 4 modules. 
Without importing anything, compute: each student's average; 
the module with the highest average; every student who failed any module (under 40).
 Done when: your output matches numbers you worked out by hand.
'''

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

student_names = ["Alice","Ben","Chloe","Daniel","Emma"]


for student_name in student_names:
    total = 0
    for student, module, mark in results:
        if student == student_name:
            total = total + mark
    average = total/4
    print ("Average mark of " + str(student_name) + " :" + str(average))
