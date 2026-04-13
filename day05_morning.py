# Task 1 — Decorators 
# A Build your first 3 decorators from scratch
from utils.formatters import timer, logger
from utils.validators import validate_positive


# Apply and test all 3:
@timer
def slow_sum(n):
    """Sum numbers 1 to n"""
    return sum(range(n))

@logger
def add(a, b):
    return a + b

@validate_positive
def multiply(a, b):
    return a * b

print(slow_sum(1000000))
print(add(5, 3))
print(multiply(4, 5))    # works
print(multiply(-1, 5))   # blocked by validator


# B Stack two decorators — apply both timer and logger to one function
@timer
@logger
def calculate_average(numbers):
    """Calculate average of a list"""
    return sum(numbers) / len(numbers)

result = calculate_average([10, 20, 30, 40, 50])
print(f"Average: {result}")

# Question: which decorator runs first — timer or logger?
# Run it, observe, write the answer in a comment
# This is asked in interviews

'''
        i assign time and then logger decorator to a function but when i run it
        loger execute first and then timer
        what i think is this is work as like
        first it call timer but in timer argument function is called 
        before it itself print any thing so from timer decorator
        logger is as argument in function and it executes then comes to the timer
        then it excecute and return result
    '''


    # C Add the timer decorator to your BankAccount methods
    # Go to your day03_morning.py BankAccount class
    # Add @timer on top of deposit() and withdraw()
    # Run a few transactions and observe the timing output
    # This is how performance profiling works in real applications

    # Expected output when you deposit:
    # "deposit took 0.0001 seconds"
    # "500 deposited"    

