## prime or not

number = int(input('enter a number'))

if number <= 1:
    print('not a prime')
    
else:
    for i in range(2,number):
        if number%i == 0:
            print(' not a prime number')
            break
    else:
        print('it prime number')

import numpy as np

#------ Given a list of numbers, create a new list that contains only the positive numbers.
digits = [i for i in range(1,21) if i %2 == 0 ]
print(digits)

sqls = [i**2 for i in range(1,11)]
print(sqls)

#------ Create a list of all even numbers between 1 and 50, but only include those that are divisible by 4.

evenls = [i for i in range(1,50) if i%4 == 0]
print(evenls)

# Given a list of words, use list comprehension to filter only those words that have more than 4 characters and convert them to uppercase.

words = ["ai", "machine", "data", "deep", "python", "sql", "code", "neural"]

newword = [temp.upper() for temp in words if len(temp)> 4]
print(newword)


# 🔹 Given a range of numbers from 1 to 10, use list comprehension to create a list of tuples where each tuple contains a number and its square. Only include tuples where the square is an even numbers

sqtup = ()

sqlist = [(i,i**2) for i in range(1,11)]
print(sqlist)


#include a,e,i,o,u, and more than 3 character
"""
words = ["AI", "OpenAI", "Intelligence", "Code", "User", "bot", "Oracle"]

vov = [ i for i in words if len(i) >3 and i[0].lower() in ('a', 'e', 'i', 'o', 'u') ]
print(vov)

#----------------------------
n = int(input('enter the N value'))
x = int(input('enter the X value'))
y = int(input('enter the Y  value'))
z = int(input('enter the Z value'))
tls = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n ]
#tls = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(tls)

"""

#Your job is to print the names of all students who scored exactly 75, in alphabetical order.

students = [
    ["Alice", 75],
    ["Bob", 80],
    ["Charlie", 75],
    ["Diana", 90],
    ["Eve", 65]
]


scored = 75

for i in students:
    print(i[0]) # 0 for names and 1 for scores 
    
"""news = []

for i in students:
    if i[1] == scored:
        news.append(i[0])
        
news.sort()
for name in news:
    print(name)
    
print(i[0])"""
