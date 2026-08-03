import cl


p1 = cl.Person()
print(p1.info())
# print(cl.Person.__name)
# print(p1.__name)

print(p1.age)
p1.age = 25
print(p1.age)
print(p1.info())