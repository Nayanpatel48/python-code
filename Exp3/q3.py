# Write a Python script to concatenate the following dictionaries to createa new one.

dictionary1 = {"x":"Nayan", "y":"Meet","j":"Hujefa", "z":"Superman", "b":"Batman", "x":"Jamun"}
dictionary2 = {"k":"kailash","p":"lop", "o":"xizo"}

def concatinate_dictionary(dictionary1, dictionary2):
    for key in dictionary2:
        dictionary1[key]=dictionary2[key]
    print(dictionary1)
concatinate_dictionary(dictionary1, dictionary2)