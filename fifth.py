 # class new:
#     def __init__(self): # initialization method. runs automatically when class is instantiated.
#         print("this is default constructor.")
# n1 = new()

# class new2:
#     def __init__(self, n, r):
#         print("this is parameterized constructor.")
#         self.name = n
#         self.roll = r
#     def call(self):
#              print(f"{self.name}'s roll no is {self.roll}.")
# n1 = new2('Stuti', 72) # method 1 of calling parameterized constructor
# n1.call()
# n1.name = 'Swara' # method 2 of calling
# n1.roll = 93
# n1.call()

# class base:
#     def __init__(self):
#         self._protec = 2
#         self.__priv = 3
# class derived(base):
#     def __init__(self):
#         base.__init__(self)
#         print("calling protected member of base class : ", 
#               self._protec)
#         print("calling private member of base class : ", 
#               self._base__priv)

#         self._protec = 4
#         self._base__priv = 5

#         print("calling modified protected member outside base class : ", 
#               self._protec)
#         print("calling modified protected member outside base class : ", 
#               self._base__priv)

# d1 = derived()

# # polymorphism
# class vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class car(vehicle):
#     def move(self):
#         print("move!")
# class boat(vehicle):
#     def move(self):
#         print("sail!")
# class plane(vehicle):
#     def move(self):
#         print("fly!")

# car1 = car("porche", "2011")
# boat1 = boat("speed", "2019")
# plane1 = plane("flew", "2017")

# for x in (car1, boat1, plane1):
#         print("brand :",x.brand)
#         print("year : ",x.year)
#         x.move()

# # value overloading
# class over:
#     def __init__(self):
#         self.value = "parent"
#         print(self.value)

# class ride(over):
#     def riding(self):
#         print(self.value)
#         self.value = "child"
#         print(self.value)

# r = ride()

# # super keyword
# class student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
# class branch(student):
#     def __init__(self, name, id, br):
#         super().__init__(name, id)
#         # self.name = name 
#         # self.id = id
#         self.br = br
# i = branch("Stuti", 72, "CO")
# print(i.name)
# print(i.id)
# print(i.br)

# # multiple inheritance
# class mother:
#     def __init__(self, mname):
#         self.name = mname
# class father:
#     def __init__(self, fname):
#         self.name = fname
# class surname:
#     def __init__(self, sname):
#         self.name = sname
# class child(mother, father, surname):
#     def __init__(self, name, mname, fname, sname):
#         self.name = name
#         # super().__init__(mname, fname, sname)
#         mother.__init__(self, mname)
#         father.__init__(self, fname)
#         surname.__init__(self, sname)
#         print(name, mname, fname, sname)
# child1 = child("stuti", "sheela", "rajkumar", "mishra")

# decorator
# def dec(func):
#     def process():
#         print("good morning.")
#         func()
#         print("farewell.")
#     return process
# @dec
# def yes():
#     print("very important message...")
# yes()

# file = open("myfile.txt", "w") 
# file.write("this is not my file.")
# file.close()

# with open("myfile.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("myfile.txt","r") as file:
#     print("reading line by line : ")
#     for line in file:
#         print(line.strip())

# with open("myfile.txt", "a") as file:
#     file.write("\nthis is appended line.")

# with open("myfile.txt","r") as file:
#     file.seek(6)
#     remaining = file.read()
#     print("content after the 6th character : ")
#     print(remaining)

# with open("myfile.txt","r+") as file:
#     file.seek(0)
#     file.write("new content written in r+ mode.\n")
#     file.seek(0)
#     content = file.read()
#     print(content)

with open("myfile.txt","w+") as file:
    file.seek(0)
    file.write("new content written in w+ mode.")
    file.seek(0)
    content = file.read()
    print(content)