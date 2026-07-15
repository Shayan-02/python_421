lst = [1, 2, 1, 1, 2, 3, 4, 3, 4, 5]
lst2 = []

for i in range(len(lst)):
    if lst[i] in lst2:
        pass
    else:
        lst2.append(lst[i])


for i in range(len(lst2)):
    print(i+1, ":", lst2[i])