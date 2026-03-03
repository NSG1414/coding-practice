class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New balance is {self.balance}"
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough funds"
        self.balance -= amount
        return f"{amount} withdrawn. New balance is {self.balance}"

        