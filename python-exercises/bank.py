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

account1 = BankAccount("Glory", 1000) 
print(account1.check_balance())
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))       