list = []
for value in range(1,11):
    list.append(value*3)

for multiple in list:
    print(multiple)

########### OR
print()

list = [value*3 for value in range(1, 11)]
for x in list:
    print(x)

