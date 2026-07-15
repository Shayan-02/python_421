lst = input().split()

a = lst
a.reverse()
print(a)

for i in range(len(a)):
    print(int(a[i]), end=" ")