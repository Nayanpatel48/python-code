# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x)

import random
import math

dictionary = {}
number = input('enter n:')
length = len(number)

variable = 1

i=0;
while i<length:
    variable= variable*10
    i=i+1

n = random.random()*variable

dictionary[int(n)]= int(n*n)
print(dictionary)