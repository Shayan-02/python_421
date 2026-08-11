d = {"name" : "ali", "age" : 20}

d["job"] = "accountant"

print(d["job"])


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(80))  # بسیار سریع‌تر از حالت بدون کش
