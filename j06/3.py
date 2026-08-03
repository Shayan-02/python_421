class Person:
    name = ""
    age = ""
    
    def showInfo(self):
        return f"your name is {self.name} and your age is {self.age} years old"

p1 = Person()
p1.name = input("enter your name person1: ")
p1.age = input("enter your age person1: ")

p2 = Person()
p2.name = input("enter your name person2: ")
p2.age = input("enter your age person2: ")


print(p1.showInfo())
print("*"*20)
print(p2.showInfo())