age = 22
height = 6.4
complex_number = 22 + 6.4j

base = int(input("Enter base: "))
height = int(input("Enter height: "))

area = 0.5 * base * height
print(area)

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimiter_triangle = side_a + side_b + side_c
print(perimiter_triangle)

length = int(input("Enter length: "))
width = int(input("Enter width: "))

perimeter_rectangle = 2 * (length + width)
print(perimeter_rectangle)

import math

radius = int(input("Enter radius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(area, circumference)

# y = mx + b, y = 2x - 2 calc slope, x int, y int

m = 2 # slope
b = -2 # y int

slope_line = m
y_intercept = (0,b)

x_value = -b / m
x_intercept = (x_value, 0)

print(slope_line, x_intercept, y_intercept)

point_a = (2,2)
point_b = (6,10)

dxx = point_a[1] - point_a[0]
dyy = point_b[1] - point_b[0]

slope_points = dxx / dyy

dx = point_b[0] - point_a[0] # 6 - 2 = 4
dy = point_b[1] - point_a[1] # 10 - 2 = 8

euclidean_distance = math.sqrt(dx ** 2 + dy ** 2)

slope_comp = slope_line - slope_points
print(slope_comp)


print(len('python')) # 6
print(len('dragon')) # 6

print(len('python') != len('dragon')) # false cuz equal

print ('on' in 'python' and 'on' in 'dragon') # true

print('jargon' in 'I hope this course is not full of jargon') # true

print(not('on' in 'dragon' and 'on' in 'python'))

print(str(float(len('python'))))

num = int(input('Enter number: '))
print(num % 2 == 0) # true if even, false if odd

print(7 // 3 == int(2.7))

print(type('10') == type(10)) # false

# print(type(int('9.8')) ==  10) # error

hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')

earnings = hours * rate_per_hour

print('Your weekly earning is ' +  earnings)

years = input('Years you have lived: ')

seconds = years * 365 * 24 * 60 * 60

print('You have lived for ' + seconds + ' seconds')

print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)