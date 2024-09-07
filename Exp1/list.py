lst = list[1,2,2,23,3,3]
print(lst)
#homogeniuos,duplication allowed, mutable
lst1 = ["kdjk","jlkd","hsfjh"]
print(lst1)
#determining the list length
#print(lst)
#lst.append(900)
#print(lst)

#l2 = ["Urvesh", "Umang"]
#lst.extend(l2)
#print(lst)
#insert method
lst1.insert(2,8989)
print(lst1)

#remove method
lst1.remove(8989)
print(lst1)

#pop method
#remove top values or latest added value or last value
print(lst1.pop())
print(lst1.pop(1))
print(lst1)

#clear method
print(lst1.clear())
print(lst1)

#list index
list3 = [1,2,3,4,5,6,3,3,3,6,7]
print(list3.index(6))
print(list3.index(3,5,8)) #searches between 5 ro 8  only
#print(list3.index(94)) throws error cause value is not present in the list

#count method +. frequency of the element
print(list3.count(3))

#Copying list
l2 = list3.copy()
list3.insert(0,898998)
print(l2)
#print(list3)

#sort and reversing
list3.sort(reverse = True)
list3.reverse()
print(list3)

l12 = [99,535,535,53,54]
l13 = [9839,7832,383928,9]
l12=l13
l14 = []
#l12 = l13 does not copy l13 into l12

#list comperehencing
#for i in l12:
#    if i % 2 == 0:
#        l14.append(i)

#print(l14)

#Comprehension => while perfomring task the list element is craeted
l45 = [898,483899,32892,93]
odd = [ i for i in l45 if i % 2 != 0]

print(odd)
mb = [ x for x in range(1,7327733288)]
print(mb)
for i in l12:
    if i % 2 == 0:
        l14.append(i)
print(l14)

#matrix 2*2
matrix = [[[2,3][4,5]]][[6,7][8,9]]
print(matrix)

#l1 = list [initial : End] ie,1:4
lst = [78,89,90,56]
lst4 = lst.index(0,3)
print(lst4)

#crate a list from l1 and l2 which contains 8 values
list1 = [1,3,7,9,13,15]#odd
list2 = [2,4,6,8,10,30]#odd
list3 = []
list3 = list1.extend(list2)
print(list3)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
list1 = [1,3,7,9,13,15]
list2 = [2,4,8,80,86]
list3 = []
sublist1 = list1[0:5]
sublist2 = list2[0:5]
list4 = sublist1+sublist2
print(list4)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
list1 = [1,3,7,9,13,15]
list2 = [2,4,8,80,86]
list3 = []
sublist1 = list1[0:5]
sublist2 = list2[0:5]
list4 = sublist1+sublist2
print(list4)

#prime number extraction from list
list5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def evenChecker (number):
    if number % 2 == 0:
        return True
    else:
        return False

print(evenChecker(3))

#prime number

def primeNumber(number):
    if number < 0 :
        number = -number
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
    if flag == True :
        print('true')
    else:
        print('false')

print(primeNumber(111))
