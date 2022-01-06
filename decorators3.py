def run_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper
@run_three_times
def print_sum(a,b):
    print(a+b)
print_sum(3,5)

def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@run_n_times(5)
def print_sum2(a,b):
    print(a+b)
print_sum2(3,6)

from functools import wraps

def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper

def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper

def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    return wrapper
  return decorator


@html('<b>', '</b>')
def hello(name):
    return 'Hello {}!'.format(name)
print(hello('Lia'))


@html('<i>', '</i>')
def goodbye(name):
    return 'Goodbye {}.'.format(name)
print(goodbye('Lia'))


@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))
print(hello_goodbye('Lia'))


def returns_dict(func):
    """Returns a dict"""
    def wrapper(func):
        result = AssertionError
        assert type(result) == dict
        return result

    return wrapper

@returns_dict
def foo(value):
    return value

try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')


def returns(return_type):
    def decorator(func):
        def wrapper(func):
            result = type
            assert type(result) == return_type
            return result
        return wrapper
    return decorator


@returns(dict)
def foo(value):
    return value

try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')