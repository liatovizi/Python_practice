
import time

def main_decorator(state):
    def validate_form(func):
        def wrapper(password, email):
            print(state)
            time.sleep(5)
            if len(password) < 6:
                return "Weak password"
            if "@" not in email:
                return "not valid"
            return func(password, email)
        return wrapper
    return validate_form


@main_decorator("validating.....")
def form(email, password):
    return "its ok"

print(form("atti", "1234567"))
print(form("posta@email.com", "12345345"))
print(form("posta@email.com", "12"))



def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())


@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("London", "Buenos Aires")

#+1
def multiply(a,b):
    return a * b

def double_arg(func):
    def wrapper(a,b):
        return func(a * 2, b * 2)
    return wrapper

@double_arg
def multi2(a,b):
    return (a * b)

print(multiply(1, 5))
print(multi2(1, 5))

