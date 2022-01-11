#return all even number
def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

check_even_list([1,2,3,4,5,6])

# Employee of the month
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)

print(employee_check(work_hours))

###
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

##Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range( 0, len(nums)-1):
        if nums [i:i+2] == [3,3]:
            return True
    return False

n= ([1, 1, 3])
m = ([ 3, 3, 1])
print( has_33(n))
print(has_33(m))


## count primes

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(50))

#########

def myfunc(*args):
    return sum(args)
print(myfunc(2,3,4,4))


#### returns a list containing only the even numbers

def even(*args):
    return [x for x in args if x % 2 == 0]

print(even(2,3,5,6))

#returns a string where every even letter is uppercase

def myfunc5(st):
    str=''
    for index, l in enumerate(st):
        if index % 2 == 1:
            str+=l.upper()
        else:
            str+=l.lower()
    return str

print(myfunc5('algo'))

#write a function that takes a list of integers and returns True if it contains 007 in order

def func99(nums):
    code = [0, 0, 7, 'a']
    for num in nums:
        if num == code[0] :
            code.pop(0)
    return len(code) == 1

sp1 = ([1, 2, 4, 0, 0, 7, 5])
sp2 = ([ 1, 0, 0, 5, 3, 7])
sp3 = ([1,2 ,3, 4, 5, 6, 5])

print(func99(sp1))
print(func99(sp2))
print(func99(sp3))

