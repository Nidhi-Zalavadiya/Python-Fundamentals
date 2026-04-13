# Week 1 self test 

# 1 Write answers to these 10 questions 
# 1. What is the difference between a list and a tuple?
'''
    list and tuples both are python object used to store structured data
    there are some differece between list and tuples
    - list are mutable and tuples are immutable
    - list uses square brackets [] to declare it's items where tuple difine by paranthesis ()

'''

# 2. What does .copy() do and why do you need it?
'''
    .copy() function create new object not reference of the given object
    we need copy when we want to modify any object without changing it's own arguments or behaviour
    when we use .copy() it creates new object with same arguments but it store in different memory location
'''

# 3. What is *args and **kwargs in a function?
'''
    *args and **kwargs used in function as argument with use of this we can pass any number of arguments to a function it will not crash
    *args arguments store the list, tuples, sets (inshort any number of positional arguments)and 
    **kwargs keyword stores dictionaries key-value pairs
'''
# 4. What is the difference between a class variable
#    and an instance variable?
'''
    -Class variable is refere to the whole class where instance variables are saperate for each instance of a class
    -class variables are define just after class and and before __init__
    instance variable define and assign in side __init__ method
    -we can use class variable with className.variable
    for instance variable need to use object of class like object.variable or self.variable inside class methods
    - but when reassign class variable with object name like object.variable = something
        at that time it creates a different saperate instance variable for that perticular object
        and won't change other object
    - when reassign the class variable with the class name like className.variable = something
        than it will change the value of that variable for all the instace of that class
        not for perticuler instance   
'''

# 5. What does super().__init__() do?
'''
    super().__init__()
    call the __init__ method of the parent class and resuse it in child class
'''
# 6. What is polymorphism — give one example from your code
'''
    polymorphism in python is band the different things in one but they actually are different
    in simple words polymorphism allows single interface (functions, methods) to behave differently

    as an example : 
    accounts = [
    BankAccount("Amit", "REG001", 1000),
    SavingsAccount("Raj", "SAV001", 2000),
    CurrentAccount("Priya", "CUR001", 500),
    ]

    for account in accounts:
        print(account)

    in above accounts stored the list of different class objects
    when print it one by one with for loop every time it run the __str__ of different class objects
    but look like same in code
'''

# 7. What is the difference between "w", "a", and "r" file modes?
'''
    "w" write mode allows to write in file , creates a file if not found, over right the content of file
    "a" append mode also allows to write in file, creates a file if not found, it will append the new content to exiting content of file at the end of file
    "r" read mode opens file in read mode, throws error fileNotFound if file can not found
'''
# 8. What does the "finally" block do?
'''
    in try, except block finally will always execute where there is any exception pr not
    it is mainly used in database connection close or close the file or remove resources at the end of the task
'''

# 9. What is a decorator and what problem does it solve?
'''
    decorator in python are used to modify or extend the behaviour of the function without changing the function it self
    deccorators solve the big headache of developers for changing the behaviour of function or difine different function
    for that work with decorator just one create function and tell what to add  and this decorator use in multiple functions 
    to chenge their behaviour
'''
# 10. What is the difference between O(n) and O(n²)?
#     Give an example from your own code
'''
    time complexity of O(n) and 0(n²) is that if i use 2 loops in my code to solve problem
    it will iterate inner loop then outer then again whole inner like it takes time to give result 
    as it iterate in 2 loops

    for example : 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    this is O(n²) 
    and 
    def twoSumSmart(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need],i]
            seen[nums[i]] = i
    this is O(n)
    time complexity as it cuts the steps to generate result
'''



'''
    bigest thing i learn in this 5 days is to solve problem if it is hard than think about problem
    why this problem occure , ways to solve problem then solution will automatically in mind
    just do not give up on any problem
    if there is problem there is solution too

    biggest surprise i can say i was very weak in file handling and decorators but by implement logic by myself
    and think about solution it surprise me that this was easy why i takes too much time to understand this

    i want to solve real world problem like train model that use to solve problems which takes too much time for human
    and also give accurate result
'''