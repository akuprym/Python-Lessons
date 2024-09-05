def my_decorator(func):
    def wrapper():
        print("Before func is called")
        func()
        print("After func is called")
    return wrapper


# One way: w/out syntaxis sugar

def say_hello():
    print("Hello!")


my_decorator(say_hello)()


# Another way, better:

@my_decorator
def say_hello():
    print("Hello!")


say_hello()
