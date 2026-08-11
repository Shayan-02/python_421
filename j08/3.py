# super class (parent class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"Hi, My name is {self.name}\nMy age is {self.age}"
    def move(self):
        return f"{self.name} is movving."

# class (child class)
class Student(Person):

    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        return super().info() + f"years old.\nMy major is {self.major}."
    def move(self):
        # return f"{self.name} is walking"
        return super().move() + f"\nmove : walk"


class Baby(Person):
    def info(self):
        return super().info() + f"months old."
    def cry(self):
        return "Baby is cryinng"
    def move(self):
        return "4 dast o pa"

print("----------------- student -------------------")

s1 = Student("john", 20, "computer")
print(s1.info())
print(s1.move())

print("----------------- baby -------------------")

b1 = Baby("ali", 3)
print(b1.info())
print(b1.cry())
