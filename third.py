# set = {1.0, 'hello', 1, 2, 3}
# print(set)

# dict = { 'name' : 'stuti',
#         'rollno' : 72,
#         'marks' : [1,2,3,4,5]}
# print(dict)

# def greet():
#     print('hello!')
#     return 'hello'
# greet()

# sqr = {x : x ** 3 for x in range(1,11) if x != 7} # dictionary comprehension
# print(sqr)
# print(sqr.items())

# list = [x for x in range(2,9) if x != 5]
# print(list)

# y = 14
# list2 = [x * y for x in range(101,122)]
# print(list2)

# list3 = [x * x for x in range(2,23,2)]
# print(list3)

# user = input("enter ")
# print(user)

# list4 = []
# n = int(input("enter n : "))
# for i in range(n):
#     val = int(input(f"value {i + 1} : "))
#     list4.append(val)
# print(list4)

def stuti(name):
    print("Hallo, " + name + ". Guten morgen! Stuti ist sehr klug und nett.")
stuti("Stuti")

# def mul(x,y):
#     c = x * y
#     return c
# x = int(input("enter x : "))
# y = int(input("enter y : "))
# p = mul(x,y)
# print(p)

# def function1():
#     n = int(input("enter n : "))
#     sum = 0
#     for i in range(n):
#         a = int(input("enter num : "))
#         sum += a
#     return sum
# res = function1()
# print(res)

# print(abs(-10.8375))

def greet(name,msg):
    print("Hallo," , name + '. ' + msg)

# greet("Stuti","Guten morgen")
# greet("Krishita","How are you?")

# def ageAvg():
#     n = int(input("enter number of students : "))
#     sum = 0
#     for i in range(n):
#         age = int(input(f"enter age of student {i+1} : "))
#         sum += age
#     avg = sum/n
#     print("average age = " , avg)
# ageAvg()

# def ageAvg():
#     n = int(input("enter number of students : "))
#     list5 = []
#     for i in range(n):
#         age = int(input(f"enter age of student {i+1} : "))
#         list5.append(age)
#     sum1 = sum(list5)
#     avg = sum1/n
#     print("average age = " , avg)
# ageAvg()

# def greetings(name = "stuti",msg = "good morning"):
#     print("hello, " + name + ". " + msg)
# defm = greetings() # default arguments
# notdefm = greetings("swara","how are you?") # user-defined arguments

# def family(*kids):
#     print("My youngest child is " + kids[-1] + ".")
#     print("My oldest child is " + kids[0] + ".")
#     print(type(kids))
#     print(kids)
# family("Krishita","Stuti","Swara") # tuple

# # function
# def adding(x,y):
#     z =  x + y
#     print(z)
# adding(1,6)

# # function as lambda
# add = lambda x,y : x + y # name = lambda arguments : task
# sub = lambda x,y : x - y
# mul = lambda x,y : x * y
# div = lambda x,y : x / y
# sqr = lambda x,y : x * x

# x = int(input("enter x : "))
# y = int(input("enter y : "))

# a = add(x,y)
# b = sub(x,y)
# c = mul(x,y)
# d = div(x,y)
# e = sqr(x,y)

# print("add = " , a)
# print("sub = " , b)
# print("mul = " , c)
# print("div = " , d)
# print("sqr = " , e)