class Bankaccount:
    balance = 0
    def __init__(self, bal):
        self.bal = bal
    def withdrow(self, amount):
        if amount > 0 and self.bal >= amount:
            self.bal -= amount