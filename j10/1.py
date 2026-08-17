class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @classmethod
    def to_standard(cls, height, weight):
        if height > 3:
            height  /= 100

        if weight > 500:
            weight /= 1000

        return cls(height, weight)

    def calculate_bmi(self):
        return self.weight / (self.height**2)


height = float(input("enter your height: "))
weight = float(input("enter your weight: "))

if height > 3 or weight > 500:
    person = BMI.to_standard(height, weight)
else:
    person = BMI(height, weight)

print("height(m): ", person.height)
print("weight(kg): ", person.weight)
print("BMI: ", person.calculate_bmi())
