from utils.formatters import timer

class BankAccount:
    '''
        Bank account class is contains data of account holder and transaction histrory
    '''
    # __init__: owner name, account number, initial balance=0
    # All amounts stored in self.balance
    # Keep a self.transactions list — record every deposit/withdrawal
    def __init__(self, owner_name, account_number, balance = 0):
        ''' This is the __init__ method for declare variables for each instance'''
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.transaction = []
    @timer
    def deposit(self, amount):
        ''' 
            This method is for deposite amount in account
        '''
        # add amount to balance
        # add to transactions: "Deposited: 500"
        # if amount <= 0: print "Invalid amount" and return
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.transaction.append(f"Deposited : {amount}")
            print(f"{amount} deposited")
    @timer
    def withdraw(self, amount):
        '''
            Withdraw amount form account
        '''
        # subtract from balance
        # add to transactions: "Withdrew: 200"
        # if amount > self.balance: print "Insufficient funds"
        # if amount <= 0: print "Invalid amount"
        if amount > self.balance:
            print(f'Insufficient funds')
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            self.transaction.append(f"Withdrew : {amount}")
            print(f'{amount} withdrew')

    def get_balance(self):
        '''
            Returns current balace
        '''
        # return current balance
        return self.balance

    def show_transactions(self):
        '''
            show each transaction line by line
        '''
        # print all transactions one by one
        for transaction in self.transaction:
            print(transaction)

    def __str__(self):
        # "Account[ACC001] | Owner: Raj | Balance: ₹1500"
        return (f'Account[{self.account_number}] | Owner: {self.owner_name} | Balance: ₹{self.balance}')

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


if __name__ == "__main__":
    acc = BankAccount("Test", "T001", 1000)
    acc.deposit(500)
    print(acc)