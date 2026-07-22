def digit(n):
    lst=[]
    total=0
    for i in range(len(n)):
        lst.append(int(n[i]))
    for i in range(len(lst)):
        total+=lst[i]
    if total>=10:
        digit(str(total))
    else:
        return total
number=input().split()
print(digit(number))




