#taking input from user
value = input("Enter number:")
value = int(value)
print(type (value))

i = 1
sum = 0
while sum < value:
    prev = i
    sum +=prev #sum = sum +i
    print(sum)