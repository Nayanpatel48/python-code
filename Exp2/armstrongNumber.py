ansList = []

#below parameter number = list pf characters of number, org_num = original number
def isArmstrong (number, org_num, len):
    count=0
    sum =0
    i=0
    while i<len:
        num=0
        if number[i] == '1':
            num = 1
        elif number[i] == '2':
            num = 2
        elif number[i] == '3':
            num = 3
        elif number[i] == '4':
            num = 4
        elif number[i] == '5':
            num = 5
        elif number[i] == '6':
            num = 6
        elif number[i] == '7':
            num = 7
        elif number[i] == '8':
            num =  8
        elif number[i] == '9':
            num = 9
        sum +=num*num*num
        i+=1
        ########################

    if sum == int(org_num):
        print("This is armstrong number.")
    else:
        print("This is not armstrong number.")


#taking input from user
value = input("Enter number:")
#value is string by default

to_array_of_value = list(value)
isArmstrong(to_array_of_value, value, len(value))