class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.sen = age
        self.balanced = "1000$"

    def showInfo(self):
        return f"your name is {self.name} and your age is {self.sen} years old\npersonalID : {self.balanced}"


# name = input()
# age = int(input())

p1 = Person("name", 20)
print(p1.showInfo())
print(p1.name)
p1.name = "reza"
print(p1.showInfo())
print(p1.balanced)