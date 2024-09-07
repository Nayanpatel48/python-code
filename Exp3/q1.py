dictionary = {"x":"Nayan", "y":"Meet","j":"Hujefa", "z":"Superman", "b":"Batman", "x":"Jamun"}

length= len(dictionary)

def ascending_sorting_by_value(dictionary, dct_len):
    # dictionary for answer
    ans_dictionary = {}

    # fetching all values from dictionary
    list1 = []
    list2 = []
    for key in dictionary:
        list1.append(dictionary[key])
    list1.sort()
    # list1 for values
    # list2 for keys

    # print(list1)
    for values in list1:
        x=list (dictionary.keys())[(list(dictionary.values()).index(values))]
        list2.append(x)

    i=0
    while i<dct_len:
        ans_dictionary[list2[i]]=list1[i]
        i=i+1
    print(ans_dictionary)

ascending_sorting_by_value(dictionary, length)