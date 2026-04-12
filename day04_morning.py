#Task 1 — File I/O: read and write 
#A Write to a file — 4 operations
# 1. Create a file called "notes.txt" and write 3 lines to it
#    "Python is powerful"
#    "I am learning every day"
#    "Day 4 - File handling"

with open("H:\\Python Fundamentals\\Day04 Flie handling\\notes.txt", 'w') as f:
    f.write("Python is powerful\nI am learning every day\nDay 4 - File handling")

# 2. Read the entire file and print it

with open("H:\\Python Fundamentals\\Day04 Flie handling\\notes.txt", 'r')as f:
    print(f.read())


# 3. Append a new line to the file without deleting existing content
#    "Added on Day 4 evening"
with open("H:\\Python Fundamentals\\Day04 Flie handling\\notes.txt", 'a') as f:
    f.write("Added on Day 4 evening")

# 4. Read the file line by line using a for loop
#    print each line with its line number:
#    "Line 1: Python is powerful"
#    "Line 2: I am learning every day"
with open("H:\\Python Fundamentals\\Day04 Flie handling\\notes.txt", 'r') as f:
    for count, content in enumerate(f, 1):
        print(f"Line {count}: {content}")


#B Work with CSV data — this is used in every ML project
def fetch_from_csv(file):
    student_data = file.readlines()
    headers = student_data[0].strip().split(',')
    student = []
    for data in student_data[1 : ]:
        row = data.strip().split(',')     
        student.append(dict(zip(headers, row)))
    return student

# 1. Write this student data to "students.csv"
students = [
    {"name": "Raj",   "age": 21, "grade": "A"},
    {"name": "Priya", "age": 22, "grade": "B"},
    {"name": "Amit",  "age": 20, "grade": "C"},
]
# Write header first: "name,age,grade"
# Then write each student as: "Raj,21,A"
with open("H:\\Python Fundamentals\\Day04 Flie handling\\students.csv", 'w') as file:
    file.write("name,age,grade")
    for data in students:
        line = f"\n{data["name"]},{data["age"]},{data["grade"]}"
        file.write(line)

# 2. Read "students.csv" back
#    Parse each line into a dictionary
#    Print each student dict
#    Output: {"name": "Raj", "age": "21", "grade": "A"}
with open("H:\\Python Fundamentals\\Day04 Flie handling\\students.csv", 'r') as file:
    student_data = fetch_from_csv(file)
    for data in student_data:
        print(data)

    
        
# 3. Count how many students have grade "A"
#    Read the file, parse it, count — print the result
with open("H:\\Python Fundamentals\\Day04 Flie handling\\students.csv", 'r') as file:
    student_data = fetch_from_csv(file)
    count = 0
    for data in range(len(student_data)):
        if student_data[data]["grade"] == "A":
            count += 1
    print(count)


#Task 2 — Exception handling 
# A Basic try/except — handle these 5 common errors
# For each one: write code that causes the error,
# then wrap it in try/except and handle it gracefully

try:
    # 1. ZeroDivisionError
    # crashes — wrap this
    result = 10 / 0 
except ZeroDivisionError:
    print("Error : Can not divide by zero")

try:
    # 2. ValueError
    number = int("hello")   # crashes — wrap this
except ValueError:
    print("Error : Invalid input - please enter a number")

try:
     # 3. FileNotFoundError
    with open("missing_file.txt", "r") as f:   # crashes — wrap this
        content = f.read()
except FileNotFoundError:
    print("Error : File Does not Exist Please Select Another File")

try:
    # 4. IndexError
    my_list = [1, 2, 3]
    print(my_list[10])   # crashes — wrap this
except IndexError:
    print("Error : List does not contains the no. elements that you mention")

try:
    # 5. KeyError
    my_dict = {"name": "Raj"}
    print(my_dict["age"])   # crashes — wrap this
except KeyError:
    print("Error : Key Does not exist in dictionary")

#  For each one print a helpful message in the except block:
# "Error: cannot divide by zero"
# "Error: invalid input — please enter a number"
# etc.


# B try / except / else / finally — use all 4 together
def divide(a, b):
    """
    Divide a by b safely
    - try: attempt division
    - except ZeroDivisionError: handle it
    - else: runs only if NO exception — print "Success"
    - finally: ALWAYS runs — print "Operation complete"
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Operation complete")

divide(10, 2)   # should print Result then Operation complete
divide(10, 0)   # should print error then Operation complete


# C Custom exception — write your own error type
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds balance"""
    def __init__(self, massage):
        self.massage = massage
        super().__init__(self.massage)

    def __str__(self):
        return self.massage


class InvalidAmountError(Exception):
    """Raised when amount is zero or negative"""
    def __init__(self, massage):
        self.massage = massage
        super().__init__(self.massage)
    
    def __str__(self):
        return self.massage

# Now use these in a simple withdraw function:
def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount} — balance is only {balance}"
        )
    return balance - amount

# Test with try/except:
try:
    new_balance = withdraw(1000, -1500)
except InsufficientFundsError as e:
    print(f"Withdrawal failed: {e}")
except InvalidAmountError as e:
    print(f"Invalid input: {e}")
else:
    print(f"New balance: {new_balance}")

