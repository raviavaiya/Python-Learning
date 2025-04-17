
def debug(func):
    def wrapper(*args,**kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwarg_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling {func.__name__} called with args: {arg_value} and kwargs: {kwarg_value}")
        return func(*args,**kwargs)

    return wrapper




@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")   


greet("Alice" , greeting="Hi") # Hi, Alice!