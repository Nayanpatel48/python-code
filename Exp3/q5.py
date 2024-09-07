# Write a Python program to iterate over dictionaries using for loops.
dictionary1 = {"x":"Nayan", "y":"Meet","j":"Hujefa", "z":"Superman", "b":"Batman", "x":"Jamun"}

def iterating_dictionary(dictionary):
    for key in dictionary:
        print("key={} value={}".format(key, dictionary[key]))

iterating_dictionary(dictionary1)