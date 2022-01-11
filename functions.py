def vol(rad):
    return 4/3 * 3.14 * (rad ** 3)

#write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('{} not in the range between {} and {}'.format(num, low, high))

print(ran_check(3, 10, 15))

#if you only wanted to return a boolean
def ran_bool(num, low, high):
    return num in range(low, high + 1)
print(ran_bool(3, 2,5))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def calc_letter(st):
    lower = 0
    upper = 0
    for i in st:
        if (i.islower()):
            lower = lower +1
        else:
            upper = upper +1
    print('{} and {}'.format(lower, upper))

print(calc_letter('ArrdD'))

#Write a Python function that checks whether a word or phrase is palindrome or not.
def mufunc3(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False
print(mufunc3('elle'))



