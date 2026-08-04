class User:
    def __init__(self, name='', phone=''):
        self.name = name
        self.__phone = phone
    def set_phone(self, phone):
        if len(phone) == 11 and phone.isdigit():
            self.__phone = phone
    def get_phone(self):
        return self.__phone
ali = User()
ali.set_phone('01234567891')
print(ali.get_phone())

print(ali.__phone)