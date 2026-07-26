# f = open(r"D:\Desktop\all\code\python\classes\classes_1405\python_421\j05\files\1.txt")
f = open(r"./files/1.txt")
print(f.read())
# print(f.readline())
print(f.readlines())

lst = f.read().split("\n")
print(lst)