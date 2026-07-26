import random

lst = ["ali", "reza", "mohammad"]

a = random.randint(0, len(lst) - 1)

print(lst[a])

b = random.choice(lst)
print(b)