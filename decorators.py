def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator  # it is equivalent to below decorator function line 18-19
def say_hi():
    return 'hello there'


print(say_hi())


decorator = uppercase_decorator(say_hi)
print(decorator())


def split_string(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string

    return wrapper


@split_string  # chained decorator and it excutes from bottom up.
@uppercase_decorator
def say_hi():
    return 'hello there'


print(say_hi())
