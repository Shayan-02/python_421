
    


lst = []

tedad = int(input())

for i in range(tedad):
    phone = input()
    lst.append(phone)

print(lst)

res = []
temp = "+98"
for i in lst:
    if len(i) == 11 and i.startswith("09") and "+" not in i:
        for _ in range(1, len(i)):
            temp += _
        res.append(temp)

