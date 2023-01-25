old_age = input("Enter the age of dhyan: ")
new_age = int(old_age) + 2
print(new_age)

# sum oftwo number
first_number = input("Enter the first number:")
second_number = input("Enter the second number:")
sum = int(first_number) + int(second_number)
print(sum)

name = "dhyan chandra"
C = name.capitalize()
print(C)
E = name.upper()
print(E)
print(name.find("chandra"))
print(name.replace("dhyan","Ram"))
print("d" in name)
print("R" in name)


# print the n natural number
n = str(input("Enter the God of all sanatani dharma:"))
for i<=n:
    print(i)

calulate 2 num
result=2+3/5
print(result)

r=2+7-(7*5)/7
print(r)

#Logic operater
print(5<4 or 6>2)
print(5<2 and 6>2)

#if elif and else case

age=int(input())
if age>=19:
    print("Your are jaban")
elif age<=17 and age>15:
    print("you are chota")
else:
    print("you are too nibaa")

#Loops case
students=["ram", "shyam", "kishna", "radha", "radhika"]
for i in students:
    if i=="radha":
        break;
    print(i)

# using break statement 
number=[1, 4, 6, 81, 20, 98, 39, 10, "dhyan", "shyam", 654]
for i in number:
    if i== 654:
        break;
   print(i) 

girlfriends=["Pooja Mishra", "Shikha singh", "Gunja tripathi", "Karismaa singh"]
for i in girlfriends:
    if i=="Karismaa singh":
        break;
    print(i)

marks=["Dhyan", "ram", 21, 9, 2.1, 2398, 46, "chandra", 44, 9.22]
for i in marks:
    if i== 9.22:
        break;
    print(i)

Cgpa=[6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
for i in Cgpa:
    if i==9.5:
        break;
    print(i)

# continue statement
#continue statement is applied for that you want left that using continue statment

number=[1, 4, 6, 81, 20, 98, 39, 10, "dhyan", "shyam", 654]
for i in number:
    if i==1:
        continue;
    print(i)

# Touple is a unmutable and in tuple only two opretion are applied
marks=(96,97,98,99,99,96)
print(marks.count(99))
print(marks.index(98))

# Set is not define index mean unorderd and not duplicate mean only one index
marks={93,99,98,98,93}
print(marks) 

# Dictinory is a key:value pair
marks={"Maths":98, "chemistry":97, "Physics":98}
print(marks)
print(marks["chemistry"])
marks["Biology"]=96
print(marks)
del marks["chemistry"]
print(marks)

# three types of funtion in python
# In-Built functions => (int, str, bool like that)
# Module functions (import math, )
# User-Defined functions

#in built function

import math
print(dir(math))

from math import sqrt
print(sqrt(9))

# here is i use * its mean all functios of Module function

from math import*
print(sqrt(16))

# user-defined funtion
# syntax of function

def function_name(parameters):
    // do somethings

# here function_name is any name fo function
# here parameter operator 

def print_sum(first, second):
    print(first + second)
print_sum(2, 5)

def print_sum(first, second):
    print(first + second)
print_sum(10,5)

def function_name(parameter):
    print(parameter)
print(function_name)



