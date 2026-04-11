#Task 1 — your first class (5:40–6:00 AM)
#A Build a Student class from scratch
class Student:
    # __init__ takes: name, age, marks (list)
    # store all three as instance variables
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average(self):
        # calculate and return average of marks
        avg = sum(self.marks) / len(self.marks)
        return avg 

    def get_grade(self):
        # return "A", "B", "C", or "F"
        # A=90+, B=75+, C=60+, F=below 60
        avg = self.get_average()
        if avg > 90:
            return ("A")
        elif avg > 75 and avg <= 90:
            return ("B")
        elif avg > 60 and avg <= 75:
            return ("C")
        elif avg <= 60:
            return ("F")

    def introduce(self):
        # return a string like:
        # "Hi, I am Raj, age 21, grade B"
        return (f'Hi, I am {self.name}, age {self.age}, grade {self.get_grade()}')

    def add_mark(self, mark):
        # add a new mark to self.marks
        self.marks.append(mark)
        
        

# Test your class — create 3 student objects
student1 = Student("Raj", 21, [85, 90, 78])
student2 = Student("Priya", 22, [92, 88, 95])
student3 = Student("Amit", 20, [70, 65, 80])

# Print introduction for each
print(student1.introduce())
print(student2.introduce())
print(student3.introduce())

# Add a new mark to student1 and print their new average
student1.add_mark(80)
print(f"New Average of {student1.name} : {student1.get_average()}")

# Print all three students' grades
print(f"{student1.name}'s Grade : {student1.get_grade()}")
print(f"{student2.name}'s Grade : {student2.get_grade()}")
print(f"{student3.name}'s Grade : {student3.get_grade()}")


#Task 2 — class variables vs instance variables (6:00–6:30 AM)
#A Understand the difference by building this
class StudentTask2:
    school_name = "Junagadh High School"  # class variable
    total_students = 0                     # class variable

    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age       # instance variable
        StudentTask2.total_students += 1  # increment on every new student

    def get_info(self):
        # return: "Raj studies at Junagadh High School"
        return (f'{self.name} studies at {StudentTask2.school_name}')

# Create 3 students
# Print total_students after each creation — watch it increment
student2_1 = StudentTask2("Nidhi",21)
print("Total Students : ", StudentTask2.total_students)
student2_2 = StudentTask2("Priya",25)
print("Total Students : ", StudentTask2.total_students)
student2_3 = StudentTask2("Aarya",19)
print("Total Students : ", StudentTask2.total_students)


# Print school_name from an object AND from the class directly
print(f'School name from an object {student2_1.name} : {student2_1.school_name}')
print(f'School name from an object {student2_2.name} : {student2_2.school_name}')
print(f'School name from an object {student2_3.name} : {student2_3.school_name}')
print(f'School name from an Class Student : {StudentTask2.school_name}')


# Change school_name for one object — does it affect others?
'''Without run below line i can say it will affect Others 
   bcs schoold name is Class veriable 
   and class veriable are always same for all the instance of that class
'''
student2_1.school_name = "PKM Collage Junagadh"
print(student2_1.school_name)
print(student2_2.school_name)
print(student2_3.school_name)
# Write a comment explaining what you observed
'''
    What i was thinking was totally different from what i get
    why?
    Yeah may be i got it 
    if i change class veriable from any pertculer object 
    it may change for it self only
    And If i change the class verible by CLass name itself 
    than it will affect all other objects too..
'''

#B Add a __str__ method — this makes your object printable
class StudentTask2B:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        # when someone does print(student1)
        # it should show: "Student: Raj | Age: 21 | Avg: 84.3"
        avg = sum(self.marks) / len(self.marks) 
        return (f'Student: {self.name} | Age: {self.age} | Avg: {avg:.2f}')

student1 = StudentTask2B("Raj", 21, [85, 90, 78])
print(student1)   # should print nicely — not <__main__.Student object>


#Mini project — Bank Account class 
#Build a complete BankAccount class
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
            self.transaction.append({"Deposited" : amount})
            print(f"{amount} deposited")

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
            self.transaction.append({"Withdrew" : amount})
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
        for transection in self.transaction:
            print(transection)

    def __str__(self):
        # "Account[ACC001] | Owner: Raj | Balance: ₹1500"
        return (f'Account[{self.account_number}] | Owner: {self.owner_name} | Balance: ₹{self.balance}')

# Test everything:
account1 = BankAccount("Raj", "ACC001")
account1.deposit(1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(5000)   # should say "Insufficient funds"
account1.deposit(-100)    # should say "Invalid amount"
print(account1)
account1.show_transactions()

account2 = BankAccount("Priya", "ACC002", 2000)
account2.withdraw(500)
print(account2)