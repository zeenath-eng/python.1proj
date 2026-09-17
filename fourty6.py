#Decorators
def decorator(func):
    def wrapper():
        print("Transaction Initiated")
        func()
        print("Transaction Completed")
    return wrapper
@decorator
def hello():
    print("Executing all the steps")
hello()