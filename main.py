# class Kalkulator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def plus(self):
#         print(f" {self.a} + {self.b} = {self.a + self.b}")
#     def minus(self):
#         print(f" {self.a} - {self.b} = {self.a - self.b}")
#     def zarb(self):
#         print(f" {self.a} * {self.b} = {self.a * self.b}")
#     def zarb2(self):
#         print(f" {self.a} ** {self.b} = {self.a ** self.b}")
#     def taksim(self):
#         print(f" {self.a} / {self.b} = {self.a // self.b}")

# # a = int(input())
# # b = int(input())
# obj1 = Kalkulator(int(input()),int(input()))
# obj1.plus()
# obj1.minus()
# obj1.zarb()
# obj1.zarb2()
# obj1.taksim()


# home work

# task 1



# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def great(self):
#         print(f"Hello, my name is {self.name}")


# person_name = Person(input())

# person_name.great()




# task 2


# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
        
#         return self.length * self.width
    
# r1 = Rectangle(5,5)
# r2 = Rectangle(10,10)

# area1 = r1.area()
# area2 = r2.area()

# print(f"The area of the first is {area1}")
# print(f"The area of the second is {area2}")




# # task 3

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return Circle.pi * (self.radius ** 2)
    
# obj1 = Circle(10)

# obj = obj1.area()

# print(obj)



# # task 4
# class Car:
#     total_cars = 0
#     def __init__(self):
#         Car.total_cars += 1
    
#     @classmethod
#     def total(cls):
#         return cls.total_cars

# c1 = Car()
# c2 = Car()
# c3 = Car()

# print(f"Total = {Car.total ()}")