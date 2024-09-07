ansList = []

for j in range(1,10000):
    flag = True
    for i in range(2,j):
        if j % i == 0:
            flag = False
    if flag == True :
        ansList.append(j)
    else:
        continue

print(ansList)