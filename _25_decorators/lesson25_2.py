def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before func is called")
        func(*args, **kwargs)
        print("After func is called")
    return wrapper

@my_decorator
def say_hello(*, name: str) -> None:
    print(f"Hello, {name}!")

# Function with argument
say_hello(name="Anna")