def mahtab(n):
    sum_numbers=0
    for i in range(1,n):
        if i%2:
            sum_numbers+=i
    print(sum_numbers)

# n=int(input())
n = 10
print(mahtab(n))