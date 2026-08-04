class BankAccount:
    def __init__(self, account_number, balance=0):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"variz : {amount}")
        self.get_balance()
    

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("bardasht :{amount")
            self.get_balance()
        if self.balance < amount:
            return f"mojudi kafi nist"

    def get_balance(self):
        print(f"ba tashakor as estefadeh shoma\nmojoodi hesab e shoma : {self.balance}$ ast.")

    def info(self):
        return f"your account number is : {self.account_number}\nyour balance is : {self.balance}"


account_number = input("enter account number: ")
balance = int(input("enter your balance: "))

account = BankAccount(account_number, balance)

question = input(
"""
what operation want to do???
1- deposit
2- withdrawal
3- get balance
4- information
: """
)
if question == "1":
    amount = int(input("mablagh:"))
    account.deposit(amount)
elif question == "2":
    amount = int(input("mablagh: "))
    print(account.withdrawal(amount))
elif question == "3":
    account.get_balance()
elif question == "4":
    print(account.info())

# print(account.deposit(500))
