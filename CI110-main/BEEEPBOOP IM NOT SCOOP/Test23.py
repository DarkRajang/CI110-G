# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))


# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))


# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result


print(my_sum(1, 2, 3))


# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# concatenate_2.py
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# mysterious_statement.py
*a, = "RealPython"
print(a)
