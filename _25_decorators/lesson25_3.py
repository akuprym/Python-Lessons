def my_decorator(func):
    def wrapper(*args, **kwards):
        print("Before func is called")
        result = func(*args, **kwards)
        print("After func is called")
        return result
    return wrapper

@my_decorator
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b

result = add_numbers(a=2, b=3)
print(result)