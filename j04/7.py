a = "9999993"

total = 0
for i in range(len(a)):
    total += int(a[i])
    while total >= 10:
        total2 = 0
        for _ in str(total):
            total2 += int(_)
        total = total2

print(total2)
