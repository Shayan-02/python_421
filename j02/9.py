a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a, b, sep="\n")

count_eye = 0
for i in range(8):
    if a[i] == b[i] == 1:
        count_eye += 1

print(count_eye)