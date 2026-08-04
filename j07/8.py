class User:
    def __init__(self, name, phone, pId):
        self.name = name
        self.phone = phone
        self.personalID = pId

    def __repr__(self):
        return (
            f"name : {self.name}\nphone : {self.phone}\npersonal ID : {self.personalID}")
    def __str__(self):
        return f"""
    name : {self.name}
    phone : {self.phone}
    personal ID : {self.personalID}
    """


u1 = User(name="ali", phone="0987654321", pId="1234567890")
# print(repr(u1))
# print("================")
# print(u1.__repr__())
# print(u1.show_info())

print(str(u1))
print("==========")
print(repr(u1))