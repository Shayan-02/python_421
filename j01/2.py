def isEven(number):
    if number == 0:
        return f"{number} is zero"
    elif number % 2:
        return f"{number} is odd"
    else:
        return f"{number} is even"

print(isEven(2))
print(isEven(3))
print(isEven(0))

a = input().split()
print(a)