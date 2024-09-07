# Write a Python script to check whether a given key already exists in adictionary.

dictionary1 = {"x":"Nayan", "y":"Meet","j":"Hujefa", "z":"Superman", "b":"Batman", "x":"Jamun"}
key=input('enter key:')
print(key)

def checking_existing_of_key(dictionary1, check_key):
    for key in dictionary1:
            if check_key == key:
                print("Key exist.")
                break

checking_existing_of_key(dictionary1, key)