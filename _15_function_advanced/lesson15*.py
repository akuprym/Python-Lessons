# Add multiple arguments to func

def add_all(*args):
    print(args)
    print(type(args))

    summary = 0
    for num in args:
        summary += num
    return summary

print(add_all(1,2,3))

# add 2 lists in one func
first_list = [1,2,3]
second_list = [4,5,6]

print(add_all(*first_list, *second_list))







