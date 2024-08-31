# Func that accepts all types of args

def func_with_all_arguments(x: int, y: int, *args, value: int = 9, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

person = {
        "name": "Anna",
        "age": 25
}

func_with_all_arguments(3, 5, 6,7,8, **person)