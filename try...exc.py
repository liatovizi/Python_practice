try:
    f = open('testfile', 'w')
    f.write('Test write this')
except IOError:
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)
askint()

####
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occurred!")

###
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')


