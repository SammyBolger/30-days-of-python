'''''''''
1. Check the python version you are using

python3 --version

2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
3 + 4
subtraction(-)
3 - 4
multiplication(*)
3 * 4
modulus(%)
3 % 4
division(/)
3 / 4
exponential(**)
3 ** 4
floor division operator(//)
3 // 4

3. Write strings on the python interactive shell. The strings are the following:
Your name
"Sammy"
Your family name
"Bolger"
Your country
"USA"
I am enjoying 30 days of python
"I am enjoying 30 days of python"

4. Check the data types of the following data:
10
type(10)
9.8
type(9.8)
3.14
type(3.14)
4 - 4j
type(4 - 4j)
['Asabeneh', 'Python', 'Finland']
type(['Asabeneh', 'Python', 'Finland'])
Your name
type("Sammy")
Your family name
type("Bolger")
Your country
type("USA")
'''''''''

# find euclidean distance between two points (2, 3) and (10, 8)

import math

point_p = (2,3)
point_q = (10,8)

dx = point_q[0] - point_p[0] # 10 - 2 = 8
dy = point_q[1] - point_p[1] # 8 - 3 = 

distance = math.sqrt(dx**2 + dy**2)
print(distance)