class User:
    def __init__(self, name, phone, pId):
        self.name = name
        self.phone = phone
        self.personalID = pId
    def set_phone(self, __ph):
        self.phone = __ph
    def get_phone(self):
        return f"your phone is {self.phone}"


