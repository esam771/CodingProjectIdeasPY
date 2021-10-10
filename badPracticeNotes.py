from enum import Enum, auto

# notes for python practices to avoid

# 1: avoid imprecise types


class Role(Enum):
    # use things like enums, can be more precise than strings
    example = auto()

# 2: avoid duplicate code


def find_type1():
    print('type one')


def find_type2():
    print('type two')

# reduce possible bug problems by making code more universal


def find_type(type_num):
    print('type', type_num)

# 3: reduce codes dependence on other code, follow fundamental OOP principles

# 4: don't pass a boolean to separate a method, make two methods


def print_num(num, boolean): # avoid this
    if boolean:
        print(num)
    else:
        print(num * 2)


def print_num1(num):  # use these
    print(num)


def print_num2(num):
    print(num * 2)

# 5: don't use exceptions if they don't do anything


try:
    print('hello')
except Exception: # building exceptions like this doesn't help anything
    pass

# just don't use try and exception in cases like this

print('hello')


