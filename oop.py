'''
Objects
In Python, everything is an object. We can check it by type()
An attribute is a characteristic of an object. A method
is an operation we can perform with the object.

__init__()-->used to initialize the attributes of an object
'''

'''
class User defined objects are created using the class
keyword. The class is a blueprint that defines the
nature of a future object. From classes we can
construct instances. An instance is a specific object
created from a particular class.

'''
class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    #methods
    def bark(self):
        print("Wooffff!!...My name is {}".format(self.name))
sam = Dog('Lab','Sam')

print(sam.name)
print(sam.species)
sam.bark()


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())


'''
Inheritance
Inheritance is a way to form new classes using classes
that have already been defined. The newly formed
classes are called derived classes, the classes that we
derive from are called base classes. Important benefits
of inheritance are code reuse and reduction of
complexity of a program. The derived classes
(descendants) override or extend the functionality of
base classes (ancestors).
'''


class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark() 
'''
Polymorphism
We've learned that while functions can take in different
arguments, methods belong to the objects they act on.
In Python, polymorphism refers to the way in which
different object classes can share the same method
name, and those methods can be called from the same
place even though a variety of different objects might
be passed in.
'''




class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Nik')
felix = Cat('Pewdie')

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)


class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
Dog1 = Dog('Shitzu')
Cat1 = Cat('Issa')

print(Dog1.speak())
print(Cat1.speak())

'''
Special Methods
Classes in Python can implement certain operations
with special method names. These methods are not
actually called directly but by Python specific language
syntax.
'''

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Cracking the Coding Interview", "Gayle", 400)

#Special Methods
print(book)
print(len(book))
del book

'''
The __init__(), __str__(), __len__() and __del__()
methods These special methods are defined by their
use of underscores. They allow us to use Python
specific functions on objects created through our class.

'''



import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
        self.x1=self.coor1[0]
        self.y1=self.coor1[1]
        self.x2=self.coor2[0]
        self.y2=self.coor2[1]
    
    def distance(self):
        self.x=pow((self.y2-self.y1),2)+pow((self.x2-self.x1),2)
        self.dis=math.sqrt(self.x)
        print(self.dis)
    
    def slope(self):
        self.slope=(self.y2-self.y1)/(self.x2-self.x1)
        print(self.slope)


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()



class Cylinder:
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        self.vol=self.pi*self.radius*self.radius*self.height
        print(self.vol)
    
    def surface_area(self):
        self.sur=(2*self.pi*self.radius*self.height)+(2*self.pi*self.radius*self.radius)
        print(self.sur)
        
c = Cylinder(2,3)
c.volume()
c.surface_area()












