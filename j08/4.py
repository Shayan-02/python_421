import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.3f} seconds")
        print(result)
        return result

    return wrapper


@timer
def sum_numbers():
    sums = 0
    for i in range(1, 1_000_001):
        sums += i
    return sums


# print(sum_numbers())
print(timer(sum_numbers()))