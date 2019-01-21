#object and class
#classes are base templete all new objects are made from.
#object just an instance of a class.Each object is unique.
#The behavior of an object is defined by its methods.
#Without class methods, a class would simply be a structure. Methods determine what type of functionality a class has, how it modifies its data, and its overall behavior
#class constructors and destructors
#Encapsulation=state can be encapsulated inside a bubble and hidden from each instance of objects
#polymorphism=same function multiple version.If a method has multiple form inside a class

import random

class Coin:
    def __init__(self, rare =False, clean = True, heads = True,**kwargs):#packdown the data into dictionary( kwargs-keyword arguments)
        for key,value in kwargs.items():
             setattr(self,key,value)#it will setup all of the states.Like setting up self.value instead of value
             
        self.is_rare = rare
        self.is_clean = clean
        self.heads=heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")
    def flip(self):
        heads_options=[True,False]
        select=random.choice(heads_options)
        self.heads=select
#defines what comes out when you print out object
    def __str__(self):
           if self.original_value >= 1:
              return "£{} Coin".format(int(self.original_value))
           else:
              return "{}p Coin".format(int(self.original_value * 100))
        

class One_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.01,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 20.3,
                "thickness": 1.52,
                "mass":3.56,
            }
        super().__init__(**data)

class Two_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.02,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 25.9,
                "thickness": 1.85,
                "mass":7.12,
            }

        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.05,
                "clean_colour":"silver",
                "rusty_colour": None,
                "num_edges" : 1,
                "diameter": 18.0,
                "thickness": 1.77,
                "mass":3.25,
            }
        super().__init__(**data)
    #polymorphism,override class
    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.10,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 1,
                "diameter": 24.5,
                "thickness": 1.85,
                "mass":6.50,
            }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour
        
class Twenty_Pence(Coin):
    def __init__(self):
        
        data = {"original_value":0.20,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 21.4,
                "thickness": 1.7,
                "mass":5.00,
            }

        super().__init__(**data)
    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Fifty_Pence(Coin):
    def __init__(self):
        
        data = {"original_value":0.50,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 27.3,
                "thickness": 1.78,
                "mass":8.00,
            }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour  



class One_Pound(Coin):#Inheritence from parent classs
      def __init__(self):
          data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour" : "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass": 9.5
            }
          #super means the parent class
          super().__init__(**data)#unpack the data from dictionary first and pack again in parent class

class Two_Pound(Coin):
    def __init__(self):
        data = {"original_value":2.00,
                "clean_colour":"gold & silver",
                "rusty_colour":"greenish",
                "num_edges" : 1,
                "diameter": 28.4,
                "thickness": 2.50,
                "mass":12.00,
            }

        super().__init__(**data)    

coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
             Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arg=[coin,coin.colour,coin.value,coin.diameter,coin.thickness,
             coin.num_edges,coin.mass]
    allval="{} - Coin Colour: {},Coin value:{},Coin diameter(mm):{}, Coin thickness(mm):{}, number of edges in coin:{}, mass(g):{}".format(*arg)
    print(allval)







