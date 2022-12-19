# output of a function is denoted by "return"

###!SECTION Make names Title Case

# f_name = "sIdDhaRTH"
# l_name = "nIGAm"

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         print("You didn't type any name")
#         return
#     return f"The name is {f_name.title()} {l_name.title()}"

# print(format_name(f_name, l_name))

###!SECTION Days in a month year exercise

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """Take a year and month and output the number of days"""  # this is a docstring (documentation for the function)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)