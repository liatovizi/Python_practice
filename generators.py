# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num ** 3


for x in gencubes(10):
    print(x)


def genfibon(n):
    """Generate a fibonnaci sequence up to n"""
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfibon(10):
    print(num)


def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()
print(next(g))
print(next(g))

s = 'hello'
for let in s:
    print(let)
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))


def num_sequence(n):
    """generate values from 0 to n"""
    i = 0
    while i < n:
        yield i
        i += 1


result = num_sequence(5)
for items in result:
    print(items)


nombres = ['Alice', 'Nexi', 'Lia', 'Johnny']
def get_length(input_list):
    for person in input_list:
        yield len(person)
for value in get_length(nombres):
    print(value)

import random
random.randint(1,10)

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)
for num in rand_num(1,10,12):
    print(num)


