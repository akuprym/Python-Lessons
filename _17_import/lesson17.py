from _17_import.math_operations import add, subtract

print(add(1,2))
print(subtract(2,1))

my_int = 1
# посмотреть приватное пространство имем модуля
print(globals().keys())

import  random

# to see methods from random
print(dir(random))