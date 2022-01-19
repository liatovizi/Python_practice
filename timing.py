def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))
print(func_two(10))

import time

start_time = time.time()
result = func_one(1000000)
end_time = time.time() - start_time
print(end_time)

start_time = time.time()
result = func_two(1000000)
end_time = time.time() - start_time
print(end_time)

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt, setup, number =100))