# decorator
def decorator(func):
    def wrapper():
        print("before the function is called.")
        func()
        print("after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")
    
say_hello()

# addition using decorator
def sum_decorator(func):
    def wrapper(a, b):
        print("before addition")
        result = func(a, b)
        print("after addition")
        return result
    return wrapper

@sum_decorator
def add(a, b):
    return a + b    

# Fix: Call the function and assign it to 'result' before printing
result = add(5, 3) 
print("Result:", result)


