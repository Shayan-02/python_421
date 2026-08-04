from random import randrange
# from typing import List


class BankAccount:
    """
    Bank account management.
    """

    all_account_numbers = list()

    def __init__(self, first_name: str, last_name: str) -> None:
        self.account_number: int = 0
        while True:
            if (an := randrange(10000, 100000)) not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.append(an)
                self.account_number = an
            break
        self.first_name = first_name
        self.last_name = last_name
        self.balance: float = 0

    def display(self) -> None:
        """
        Show account balance.
        :return:
        """
        print(40 * "-")
        print(f"Hi, {self.first_name}.\nYour current balance is: {self.balance} ")
        print(40 * "-")

    def deposit(self) -> None:
        """
        Increase account balance.
        :return:
        """
        amount = float(input("Please enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        withdraw from bank account.
        :return:
        """
        amount = float(input("Please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.display()
