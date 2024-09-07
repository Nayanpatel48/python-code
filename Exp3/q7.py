# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are the square of the
# keys.
dictionary = {}

i=1
while i <=15:
    dictionary[i]=i*i
    i=i+1

print(dictionary)