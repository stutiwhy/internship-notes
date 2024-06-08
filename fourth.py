# # slicing (?)
# list = [1,2,3,4,5]
# print(list[2:]) # prints index 2 value and all values after index 2
# print(list[:3])
# print(list[2:4])

# tuple = (3,2,1,4,5,6)
# print(tuple[5:])

# for i in tuple:
#     print(i)

# # break pass continue
# str = 'apple'
# for i in str:
#     if i == 'p':
#         continue
#     else:
#         print(i)

# for i in str:
#     if i == 'a':
#         break
#     else:
#         print(i)

# for i in str:
#     if i == 'p':
#         pass
#     else:
#         print(i)

# list = [1,2,3,4,5,6,7]
# for i in range(1,15):
#     if i in list:
#         pass
#     else:
#         list.append(i)
# print(list)

# # recursion
# def search(name,i):
#     ii = i
#     list = ['stuti','swara','krishita','varsha']
#     if list[ii] is name:
#         print(f"name found at index {i}.")
#     else:
#         ii += 1
#         search(name,ii)
# search('swara',0)

# # object oriented programming in python
# # class

# class Classroom:
#     student = ["Stuti", "Swara","Krishita"]
#     teacher = "P"
# obj1= Classroom # creation and initialization of object
# print(obj1.teacher)
# print(obj1.student[2])

# class Me:
#     name = 'Stuti'
#     roll = 72
#     dept = 'CO'

#     def display(self):
#         print(f"My name is {self.name} and my roll number is {self.roll}. I am from {self.dept} department.")

# krish = Me()
# krish.name = 'Krishita'
# krish.roll = 27
# krish.display()

# stuti = Me()
# stuti.display()

# swara = Me()
# swara.name = 'Swara'
# swara.roll = 93
# swara.display()

# # inheritance
# # single inheritance
# class Bird:
#     def init(self):
#         print('Bird is ready')
    
# class Penguin(Bird):
#     def init(self):
#         super().init()
#         print("Penguin is ready.")

# krish = Penguin()
# krish.init()

# # polymorphism
# # same function used on different datatype
# list = [1,2,3,4,5,6]
# str = "STUTI"
# print(len(list))
# print(len(str))

# nums = [3,3,5,6,78,3,2,2,4,5,6,8,8,42,1,2,35,45,32,4]
# val = 3
# res = [nums[i] for i in range(len(nums)) if nums[i] != val]
# print(res)