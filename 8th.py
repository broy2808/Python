#object and class
#classes are base templete all new objects are made from.
#object just an instance of a class.Each object is unique.
#The behavior of an object is defined by its methods.
#Without class methods, a class would simply be a structure. Methods determine what type of functionality a class has, how it modifies its data, and its overall behavior
#class constructors and destructors
#Encapsulation=state can be encapsulated inside a bubble and hidden from each instance of objects
import random



class Pound:

    def __init__(self,rare=False):#constructor method.Self refers to specific instance of class
        self.rare=rare

        if self.rare==True:
            self.value=1.25
        else:
            self.value=1.00

        self.color="gold"
        self.num_edges=1
        self.diameter= 22.5#mm
        self.thickness=3.15#mm
        self.heads=True
       
    #we need to put self in every method in class
    def rust(self):
        self.color="greenish"
    def clean(self):
        self.color="gold"
    def flip(self):
        heads_options=[True,False]
        select=random.choice(heads_options)
        self.heads=select

    #destructor called automatically and destruct the object
    def __del__(self):
        print("Coin spent!")
  
coin1=Pound(rare=True)
coin2=Pound()
print(coin1.value)
print(coin1.color)
coin2.rust()
print(coin2.color)
print(coin2.value)
coin2.clean()
print(coin2.color)
coin2.flip()
print(coin2.heads)

del coin1



