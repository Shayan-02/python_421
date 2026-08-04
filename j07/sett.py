class Test:
    x = 10
    _x = 20
    __x = 30

x = 50
_x = 20

t1 = Test()
print(t1.x)
print(t1._x)
# print(t1.__x)