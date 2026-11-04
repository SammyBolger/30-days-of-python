# day 2: 30daysofpython challenge

first_name = "sammy"
last_name = "bolger"
full_name = "sammy bolger"
country = "USA"
city = "apple valley" 
age = 22
year = 2026
is_married = False
is_true = True
is_light_on = True

# level 2

print(type(first_name))
# ...

diff = len(first_name) - len(last_name)
print(diff)

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

import math

radius = 30

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(area, circumference)

user_radius = float(input('Input radius: '))
user_area = math.pi * user_radius ** 2
print(user_area)

user_first_name = input("What is your first name: ")
user_last_name = input("What is your last name: ")
user_country = input("What country are you from?: ")
user_age = int(input("What is your age: "))

print("User's name is " + user_first_name + " " + user_last_name + " and he is " + str(user_age) + " years old from " + user_country)
# f string: print(f"User's name is {user_first_name} {user_last_name} and he is {user_age} years old from {user_country}")