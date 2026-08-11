def s(a, b):
    global r
    r = a + b
    return r


print(s(10, 20))
print(s(20, 30))
print(r)

