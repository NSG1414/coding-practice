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
        
    def check_balance(self):
        return f"{self.owner}'s balance is {self.balance}"
        
    def transfer(self, amount, other_account):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        other_account.balance += amount
        return f"{amount} transferred from {self.owner} to {other_account.owner}"
        
account1 = BankAccount("Glory", 1000) 
account2 = BankAccount("Elijah", 500)

print(account1.transfer(300, account2))
print(account1.check_balance())
print(account2.check_balance())
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))       
print()