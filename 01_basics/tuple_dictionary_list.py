# # python dictionary

# # create a dictionary 
# # below name is key and Nayan is value
# # we can use any object in the place of value
# dictionaryNumberOne = {'name':'Nayan','rollnumber':220200143048}
# print(dictionaryNumberOne)

# # Access value using key name
# print(dictionaryNumberOne['name'])

# # get() method
# # x=dictionaryNumberOne.get('rollnumber')
# # print(x)
# print(dictionaryNumberOne.get('rollnumber'))

# # beofe adding new key value pair
# print(dictionaryNumberOne)

# # After adding new key value pair
# dictionaryNumberOne['gender']='male'
# print(dictionaryNumberOne)

# y = dictionaryNumberOne.values()
# print(y)

# z=dictionaryNumberOne.items()
# print(z)

# # removing item
# print('before removing element:')
# print(dictionaryNumberOne)

# print('After removing element:')
# dictionaryNumberOne.pop('name')
# print(dictionaryNumberOne)

# # Addig item
# dictionaryNumberOne['address']='valasad'
# dictionaryNumberOne['name']='Nayan'
# print('after adding value:')
# print(dictionaryNumberOne)

# # for loop
# # for key in dictionaryNumberOne.keys:
# #     print(key)

# # updating key value pair
# dictionaryNumberOne.update(
#     {'name':'Mohit'}
# )
# print(dictionaryNumberOne)

# newDictionary = dictionaryNumberOne.copy()
# print(newDictionary)
# dictionaryNumberOne.clear()
# print(dictionaryNumberOne)
# print(newDictionary.get('name'))

# print(newDictionary.items())
# print(newDictionary.keys())

# dict1 ={1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}


# dict2 =dict1.copy()

# print(dict2)

# dict1.clear()

# print(dict1)

# print(dict2.get(1))

# print(dict2.items())
# print(dict2.keys())
# dict2.pop(4)
# print(dict2)
# dict2.popitem()
# print(dict2)
# dict2.update({3: "Scala"})
# print(dict2)
# print(dict2.values()) 

# create a list for keys <-list1
# create a another list for values of keys of list

# list1 = [1,2,3,4]
# list2= ['naan', 'jja','jkj','ha']

# dctionary = {list1,list2}
# print(dctionary)

# # list is mutable and tuple if not mutable
# myTuple = ('a','b','c')
# print(myTuple)

# # lenghth of tuple
# print(len(myTuple))

# # print(type(myTuple))
# # tuple does not allow add new values

# # myTuple = ('a','b','c')
# # print(myTuple[-1]) 
# newtuple=myTuple = ('a','b','c')+('a','b','c')
# print(newtuple)
# # making new tuple after adding two tuples

# t1=newtuple*3
# print(t1)

# print(t1[::-1])
# print(t1[2::-1])

# deleting tuple in python
t1 = (1,2,3,4)
t1= list(t1)
# casting it cause immutable
t1.remove(1)
print(t1)

for t in t1:
    print(t)