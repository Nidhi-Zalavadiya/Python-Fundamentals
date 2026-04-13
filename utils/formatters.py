# Decorator 1: timer — measures how long a function takes
import time
def timer(func):
    '''
        print how much time it takes to excecute the function and 
        return the result of called function which is pass as argument in decorator
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Decorator 2: logger — prints function name and arguments before running
def logger(func):
    def wrapper(*args, **kwargs):
        # print: "Calling function_name with args=(1,2) kwargs={}"
        print(f'Calling function_name with args={args} kwargs={kwargs}')
        # then call the function and return its result
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper