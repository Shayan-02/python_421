def fact(n: int):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

def fact2(n: int):
    if n == 1:
        return 1
    else:
        n * fact2(n - 1)