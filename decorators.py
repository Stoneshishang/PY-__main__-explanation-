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

print('-------------------------------------------')

# Applying Multiple Decorators to a Single Function


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

print('-------------------------------------------')


# Accepting Arguments in Decorator Functions
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print('My arguments are: {0}, {1}'.format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))


cities("Nairobi", "Accra")

print('-------------------------------------------')

# Defining General Purpose Decorators


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")


function_with_no_argument()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)

print('-------------------------------------------')


# Passing Arguments to the Decorator
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2, decorator_arg3,
                          function_arg1, function_arg2, function_arg3))
            return func(function_arg1, function_arg2, function_arg3)

        return wrapper

    return decorator


pandas = "Pandas"


@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
          " {1}" " {2}".format(function_arg1, function_arg2, function_arg3))


decorated_function_with_arguments(pandas, "Science", "Tools")
