'''
Please write a program which prints out the following lines exactly as they are written here, punctuation and all:

Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.
'''
print("Row, row, row your boat,\nGently down the stream.\nMerrily, merrily, merrily, merrily,\nLife is but a dream.")

'''
Please write a program which prints out the number of minutes in a year.

'''
print("Minutes in a year:",365*24*60)

'''
Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.

An example of the how the program should function:

What is your name? Paul
Paul
Paul

'''
# Write your solution here
name = input("what is your name? ")
print(f'{name}\n{name}')
#print(name,"\n",name,sep='')

'''
Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.

The program should function as follows:

What is your name? Paul
!Paul!Paul!
'''
# Write your solution here
name = input("what is your name? ")
print(f'!{name}!{name}!')
#print('!',name,'!',name,'!')

'''
Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

Given name: Steve
Family name: Sanders
Street address: 91 Station Road
City and postal code: London EC05 6AW
Steve Sanders
91 Station Road
London EC05 6AW
'''
# Write your solution here
fn = input("Given name: ")
ln = input("Family name: ")
adr = input("Street address: ")
cp = input("City and postal code: ")
print(fn,ln)
print(adr + "\n" + cp)

'''
Here is a program which should ask for three utterances and print them out, like so:

The 1st part: hickory
The 2nd part: dickory
The 3rd part: dock
hickory-dickory-dock!
'''
# Fix the code
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1, part2 , part3 + '!', sep='-')
#print(part1 + "-" + part2 + "-" + part3 + "!")

'''
Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

Sample output
Please type in a name: Mary
Please type in a year: 1572

Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.

'''
# Write your solution here

name = input("please type your name: ")
year = input("please type a year: ")
print (f"{name} is a valiant knight, born in the year {year}. One morning {name} woke up to an awful racket: a dragon was approaching the village. Only {name} could save the village's residents.")

'''
my name is Tim Tester, I am 20 years old

my skills are
 - python (beginner)
 - java (veteran)
 - programming (semiprofessional)

I am looking for a job with a salary of 2000-3000 euros per month
'''
# Write your solution here

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000
 
print(f"my name is {name}, I am {age} years old")
print("")
print("my skills are")
print(" -", skill1, "("+level1+")") #use , and + as required to avoid auto white space. Alternatively we can provide print with an additional argument , sep=""  or  end = ""
print(" -", skill2, "("+level2+")")
print(" -", skill3, "("+level3+")")
print("")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

print(f"my name is {name}, I am {age} years old\n\nmy skills are\n - {skill1} ({level1})\n - {skill2} ({level2})\n - {skill3} ({level3})\n\nI am looking for a job with a salary of {lower}-{upper} euros per month")

'''
4 + 9 = 13
4 - 9 = -5
4 * 9 = 36
4 / 9 = 0.4444444444444444
'''
x = 27
y = 15
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {float(x/y)}") #float is optional, notice {} only comes once for outer function and not required in innner functions again
# Printing can also be made as follows:
#print(x, "/", y, "=", (x / y))

"""
If a single one of the operands in an expression is a floating point number, the result will also be a floating point number, regardless of the other operands.
/	Division (floating point result)	9 / 2	4.5
//	Division (integer result)	9 // 2	4
%	Modulo	9 % 2	1
**	Exponentiation	2 ** 3	8

input command reads in strings from the user, which needs to be converted to int or float. 

sum = sum + number
sum += number
"""
#Make sure to use int or float with input function when asking use for a number

'''
Please write a program which asks the user for a number. The program then prints out the number multiplied by five.
'''
# Write your solution here
x = int(input("Please type in a number: "))
print(f"{x} times 5 is {x*5}")

'''
Please write a program which asks the user for their name and year of birth. The program then prints out a message with age as of 2021
'''
# Write your solution here
name = input("What is your name? ")
age = int(input("Which year were your born?"))
print(f"Hi {name}, you will be {2021-age} years old at the end of the year 2021")

'''
Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.
'''
# Write your solution here
days = int(input("How many days? "))
print(f"Seconds in that many numbers of days: {days*24*60*60}" )

'''
This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. 
'''
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print("The product is", product)
#1
product = 1 #best practice to avoid having wrong starting point, but we can also directly go with the next line as, product = int(input())
product *= int(input("First number: ")) 
product *= int(input("Second number: "))
product *= int(input("Third number: "))
print(f"The product of the numbers: {product}")
#2
sum = 0
number = int(input("First number: "))
sum += number
number = int(input("Second number: "))
sum += number
number = int(input("Third number: "))
sum += number
print(f"The sum of the numbers: {sum}")

'''
Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.
'''
# Write your solution here
number1=int(input("first number: "))
number2=int(input("second number: "))
print("The sum of the numbers:", number1+number2)
print("The product of the numbers:", number1*number2)

'''
Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.
'''
# Write your solution here
sum = 0
sum += int(input("input first number"))
sum += int(input("input second number"))
sum += int(input("input thrid number"))
sum += int(input("input forth number"))
print(f"The sum of the numbers is {sum} and the mean is {sum/4}")

'''
Please write a program which estimates a user's typical food expenditure.
The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
'''
# Write your solution here
cafe_times = int(input("How many times a week do you eat at the student cafeteria? "))
cafe_price = float(input("The price of a typical student lunch? "))
grocery_price = float(input("How much money do you spend on groceries in a week? "))
weekly_expense = cafe_times * cafe_price + grocery_price
print(f"Avegarge food expenditure:\nDaily: {weekly_expense/7} euros\nWeekly: {weekly_expense} euros")

'''
The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
Based on this information the program calculates the user's typical food expenditure both weekly and daily.
'''
# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
print(f"Number of groups formed: { students//group_size + (students % group_size > 0)}") #() gets evaluated first
#print(students % groups > 0) # if condiation which gives answer as TRUE/FALSE which gets convered to 1/0 while using with int or sum
"""
#1
groups = (students + group_size - 1) // group_size #same logic without if, think with 11 & 3 and 12 & 4 examples
print(groups)
#2
If working with integers, one way of rounding up is to take advantage of the fact that // rounds down: Just do the division on the negative number, then negate the answer. No import, floating point, or conditional needed.

rounded_up = -(-numerator // denominator)
#3
#
import math
print(math.ceil(students/group_size))
"""

'''
Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
'''
# Write your solution here
year = int(input("Please type a number: "))
if year == 1984:
    print("Orwell")
    
'''
Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.
'''
# Write your solution here
number = int(input("Please type in a number: "))
if number < 0:
    number = number * -1
print("The absolute value of this number is", number)  #this will print for both if & else, no need to specify else if no other operation - instead use print w/o indent
"""
number = int(input("Please input an integer: "))
if number < 0:
    print("The absolute value of this number is", number * -1)
else:
    print("The absolute value of this number is", number)
"""

'''
Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.
'''
# Write your solution here
name = input("Please tell me your name: ")
if name != "Jerry":
    portions = float(input("How many portion of soup? "))
    print(f"The total cost is {5.90 * portions}")
print("Next please!")

'''
Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.
'''
# Write your solution here
number = int(input("Please type a number: "))
digits = len(str(number))
if digits > 3:
    pass
digits = 3
while digits > 0:
    print("This number is smaller than", 10**digits)
    digits -= 1
print("Thank you!")
"""
#we can use multiple ifs to print all previous outputs, as opposed to elif which checks exculsivity
number = int(input("Please type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")

number = int(input("Please type a number: "))
digits = len(str(number))
while digits > 0: #and (number < 10**digits):
    print("This number is smaller than", 10**digits)
    digits -= 1
print("Thank you!")
"""
#speed efficient -> int(math.log10(n)+1) , You will have to handle 0 separately
#digits = lambda n: sum([i.isdigit() for i in str(n)])

'''
Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.
'''
# Write your solution here
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
op = input("Operation (add/multiply/subtract): ")

if op == "add":
    print(f"{n1} + {n2} = {n1+n2}")
elif op == "multiply":
    print(f"{n1} * {n2} = {n1*n2}")
elif op == "subtract":
    print(f"{n1} - {n2} = {n1-n2}")
    
'''
Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!"
'''
# Write your solution here
f = float(input("Please type in a temperature (F): "))
d = (f - 32)*5/9
print(f"{f} degrees Fahrenheit equals {d} degrees Celsius")
if d < 0:
    print("Brr! It's cold in here!")

'''
Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
'''
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")
if weekday == "Sunday":
    # The salary is double on Sundays
    hourly_wage *= 2
total_wage = hourly_wage * hours_worked
print(f"Daily wages: {total_wage} euros")

'''
This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:
If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.
'''
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
print("You now have", points, "points")
"""
#or create new variable for mutual exculsive with only ifs
points = int(input("How many points are on your card? "))
if points < 100:
    factor = 1.1
    print("Your bonus is 10 %")
    
if points >= 100:
    factor = 1.15
    print("Your bonus is 15 %")
 
# a *= b is the same thing as a = a * b
points *= factor
print("You now have", points, "points")
"""

'''
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.
'''
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temperature < 21:
    print("I recommend a jumper as well")
if temperature < 11:
    print("Take a jacket with you")
if temperature < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
"""
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
if temp > 20:
    print("Wear jeans and a T-shirt")
elif temp > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif temp > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
else:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually\nI think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
"""

'''
Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above formula will always work.
'''
from math import sqrt # Note that the square root can also be calculated using power. sqrt(9) is equivalent to 9 ** 0.5

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

y = sqrt(b**2 - 4*a*c)

print(f"The roots are {(-b+y)/(2*a)} and {(-b-y)/(2*a)}")  #note /2*a != /(2*a)