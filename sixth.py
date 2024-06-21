exception handling
try - except syntax: 
try:
    pass
except Exception as e:
    print(e)
try:
    # print(9 / 0)
    # print(y)
    
    a = input("Enter a : ")
    # a = int(a)
    b = a * a
    print(b)
except Exception as e:
    print(e)
finally:
    print("Good bye !")

types of errors
IOError

try:
    # with open("non_existent_file.txt", "r"):
    #     content = file.read() # IOError

    n = int("hehe") # ValueError

    # res = '2' + 2 # TypeError
    
    # Logging.log(round(24.234 / 3.92, 5)) # module(????)

except IOError as i:
    print("IOError")
except ValueError as v:
    print("ValueError")
except ArithmeticError as a:
    print("ArithmeticError")
except TypeError as t:
    print("TypeError")
except FloatingPointError as f:
    print("FloatingPointError")
finally:
    print("Good bye !")

installed pip and pandas

from third import greet
greet("Stuti", "You are amazing !")

from package import mod1 as m
x = m.mul(5,9)
print(x)

from package.pack1 import *
print(mod2.add(3,8))
print(mod3.sub(3,8))
