from bank import BankAccount

def bankApp():
    account1 = BankAccount('Ali', 'Ahmadi')
    print(40 * '*')
    print(f'account number: {account1.account_number}')
    print(40 * '*')
    account1.display()
    while True:
        choice = int(input('Enter\n1 to see your balance,\n2 to deposit,\n'
        '3 to withdraw,\n4 to exit.\n\t\t your choice: '))
        if choice == 1:
            account1.display()
        elif choice == 2:
            account1.deposit()
        elif choice == 3:
            account1.withdraw()
        elif choice == 4:
            break
        else:
            print('please enter a valid number!')


if __name__ == '__main__':
    bankApp()