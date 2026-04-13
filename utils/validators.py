# Decorator 3: validator — checks that all numeric args are positive
def validate_positive(func):
    def wrapper(*args, **kwargs):
        # check every arg in args
        # if any arg <= 0: print "Error: all values must be positive" and return None
        # else: call the function normally
        if any(a <= 0 for a in args):
            print("Error: all values must be positive")
            return None
        else:
            func(*args, **kwargs)
            return func(*args, **kwargs)
    return wrapper