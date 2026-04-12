#Task 1 — Inheritance: SavingsAccount and CurrentAccount 
#A SavingsAccount — extends BankAccount with interest
from day03_morning import BankAccount

class SavingsAccount(BankAccount):
    """
    SavingsAccount is a BankAccount with:
    - interest_rate (default 4.0 percent per year)
    - minimum_balance (default 500)
    - withdraw should be blocked if balance goes below minimum
    """

    def __init__(self, owner_name, account_number,
                 balance=0, interest_rate=4.0):
        # use super() to call BankAccount __init__
        # then add interest_rate and minimum_balance as instance variables
        super().__init__(owner_name, account_number, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = 500

    def add_interest(self):
        """Calculate and deposit annual interest into the account"""
        # interest = balance * interest_rate / 100
        # deposit that amount
        # add to transactions: "Interest added: 40.0"
        interest = round(self.balance * self.interest_rate / 100, 2)
        self.balance += interest
        self.transaction.append(f"Interest added: {interest}")

    def withdraw(self, amount):
        """Override withdraw — block if balance goes below 500 after withdrawal"""
        # if balance - amount < 500: print "Cannot withdraw — minimum balance is 500"
        # else: call parent withdraw using super()
        if self.balance - amount < self.minimum_balance:
            print("Cannot withdraw — minimum balance is 500")
        else:
            super().withdraw(amount)

    def __str__(self):
        # "SavingsAccount[ACC001] | Owner: Raj | Balance: ₹1500 | Rate: 4.0%"
        return f"SavingAccount[{self.account_number}] | Owner: {self.owner_name} | Balance : ₹{self.balance} | Rate : {self.interest_rate}"

# Test:
savings = SavingsAccount("Raj", "SAV001", 2000)
savings.deposit(500)        # inherited from BankAccount — works automatically
savings.withdraw(1800)      # should block — goes below 500 minimum
savings.withdraw(500)       # should work — balance stays at 2000
savings.add_interest()      # adds 4% of 2000 = 80
print(savings)
savings.show_transactions() # inherited — works automatically

#B CurrentAccount — extends BankAccount with overdraft
class CurrentAccount(BankAccount):
    """
    CurrentAccount is a BankAccount with:
    - overdraft_limit (default 10000) — can go negative up to this limit
    - transaction_fee (default 5) — charged on every withdrawal
    """

    def __init__(self, owner_name, account_number,
                 balance=0, overdraft_limit=10000):
        # use super() to call BankAccount __init__
        # add overdraft_limit and transaction_fee=5
        super().__init__(owner_name,account_number,balance)
        self.overdraft_limit = overdraft_limit
        self.transaction_fee = 5

    def withdraw(self, amount):
        """Override withdraw — allow overdraft up to limit, charge fee"""
        # total needed = amount + transaction_fee (5)
        # if balance - total_needed < -overdraft_limit: print "Overdraft limit exceeded"
        # else: deduct total, record "Withdrew: X (fee: 5)" in transactions
        total_withdraw = amount + self.transaction_fee
        if self.balance - total_withdraw < -self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= total_withdraw
            self.transaction.append(f"Withdrew: {amount} (fee: {self.transaction_fee})")


    def __str__(self):
        # "CurrentAccount[ACC002] | Owner: Priya | Balance: ₹500 | Overdraft: ₹10000"
        return (f"CurrentAccount[{self.account_number}] | Owner : {self.owner_name} | Balance : ₹{self.balance} | Overdraft : {self.overdraft_limit}")

# Test:
current = CurrentAccount("Priya", "CUR001", 1000)
current.deposit(500)         # inherited
current.withdraw(1400)       # works — total with fee = 1405, balance = 95
current.withdraw(10000)      # should exceed overdraft limit
print(current)
current.show_transactions()



# Create one of each account type
accounts = [
    BankAccount("Amit", "REG001", 1000),
    SavingsAccount("Raj", "SAV001", 2000),
    CurrentAccount("Priya", "CUR001", 500),
]

# Loop through all accounts and print each one
# Python automatically calls the right __str__ for each type
for account in accounts:
    print(account)

# This is polymorphism — same loop, different behaviour per type
# Write a comment explaining what you observed
# i don't know please explain