#LINK - FizzBuzz Job interview question (Print 1-100 on separate lines but if number is divisible by 3, print Fizz, if divisible by 5, print Buzz, if divisible by both 3 and 5, print FizzBuzz)
# for num in range(1,101):
#   if num % 15 == 0:
#     print('FizzBuzz')
#   elif num % 3 == 0:
#     print('Fizz')
#   elif num % 5 == 0:
#     print('Buzz')
#   else:
#     print(num)

#LINK - Sum even numbers from 1 to 100 using range and for loops
# total = 0
# for number in range(2,101,2):
#   total += number

# print(total)

#LINK - Highest score using for loops

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# #Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print(f'The highest score in the class is {highest_score}')


#LINK - Average height using for loops

# # 🚨 Don't change the code below 👇
# # student_heights = input("Input a list of student heights ").split()
# student_heights = ['156', '178', '165', '171', '187']
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# print(student_heights)
# sumofheights = 0
# numberofheights = 0

# for height in student_heights:
#   # print(height)
#   sumofheights += height
#   numberofheights += 1

# averageHeight = round(sumofheights/numberofheights)
# print(averageHeight)

# # print(f'Average height is ' + str(round(sumofheights/len(student_heights))))