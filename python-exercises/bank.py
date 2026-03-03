class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amoount):
        self.balance += amount
        return f"{amount} deposited. New balance is {self.balance}"