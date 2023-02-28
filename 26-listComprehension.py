
import random
import pandas as p

numbers = [1, 2, 3]

new_list = [n+20 for n in numbers]

print(new_list)

name = "Siddharth"

new_list = [letter for letter in name]
print(new_list)

scale = range(1,5)
new_list = [num * 2 for num in scale]
print(new_list)

names = ["alex", "beth", "paige", "travis", "scott", "joe"]

short_names = [name.upper() for name in names if len(name)>4]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)

names = ["alex", "boris", "cameron", "dorothy", "elizabeth"]

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
print(passed_students)

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

student_dict = {
    "student": ["Alpha", "Beta", "Carl"],
    "score": [50, 65, 98]
}

student_dataframe = p.DataFrame(student_dict)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row.student)