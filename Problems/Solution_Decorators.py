#Timing Function Execution
# Write a decorator that measures the time a function takes to execute.

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} run in {end - start} time")
#         return result
#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)


# def greetings(func):
#     def wrapper():
#         print("Hello!")
#         func()
#         print("Goodbye!")
#     return wrapper

# @greetings
# def hello():
#     print("My Name is John Doe")

# hello()


def logger(func):
    def wrapper():
        print(f"Function {func.__name__} is called")
        func()
        print(f"Function {func.__name__} is finished")
    return wrapper

@logger
def greet():
    print("Hello!")

greet()