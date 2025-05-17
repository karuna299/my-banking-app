class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposited amount must be positive")
        self.balance += amount

    def withdrawal(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficent Funds")
        self.balance -= amount
