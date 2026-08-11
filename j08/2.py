class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Balance: ${self.__balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Added interest: ${interest}")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.__interest_rate * 100}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() + self.__overdraft_limit >= amount:
            if self.get_balance() >= amount:
                super().withdraw(amount)
            else:
                overdraft = amount - self.get_balance()
                super().withdraw(self.get_balance())
                print(f"Used overdraft: ${overdraft}")
        else:
            print("Invalid withdrawal amount or exceeded overdraft limit")

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: ${self.__overdraft_limit}")


# Testing the classes
if __name__ == "__main__":
    savings = SavingsAccount("SA001", 1000, 0.05)
    checking = CheckingAccount("CA001", 2000, 500)

    print("Savings Account:")
    savings.display_info()
    savings.deposit(500)
    savings.withdraw(200)
    savings.add_interest()
    savings.display_info()

    print("\nChecking Account:")
    checking.display_info()
    checking.deposit(300)
    checking.withdraw(2500)
    checking.display_info()
