#Task 1 — Inheritance: SavingsAccount and CurrentAccount 
#A SavingsAccount — extends BankAccount with interest
from models.bank_account import BankAccount, SavingsAccount, CurrentAccount


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