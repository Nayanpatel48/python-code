# Write a Python program to multiply all the items in a dictionary.
dictionary1 = {"x":"Nayan", "y":"Meet","j":"Hujefa", "z":"Superman", "b":"Batman", "x":"Jamun"}

multiply_ans=""

for key in dictionary1:
    multiply_ans= multiply_ans+dictionary1[key]
    
print(multiply_ans)