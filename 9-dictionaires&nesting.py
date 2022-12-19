# Dictionary is a key value pairs construct, you can nest lists or dictionaries within a dictionary


###!SECTION Exercise

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(name, timesVisited, citiesVisited):
    dict = {
        "country": name,
        "visits": timesVisited,
        "cities": citiesVisited,
    }
    travel_log.append(dict)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


###!SECTION Nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # nesting dictionary in a dictionary

# travel_log = {
#     "France": {'cities_visited':["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits":16, "nice_weather": True}
# }

# print(travel_log["France"])
# print(travel_log["Germany"]["total_visits"])

# # nesting dictionary in a list
# travel_log = [
#     {
#         "country": "France", 
#         'cities_visited':["Paris", "Lille", "Dijon"], 
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits":16,
#         "nice_weather": True,
#     }
# ]
# print(travel_log[1]["total_visits"])


###!SECTION Student scores and corresponding grades

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
    

# # 🚨 Don't change the code below 👇
# print(student_grades)