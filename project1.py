import random
import math

health=50

difficulty=3
potion_health=int(random.randint(25,50)/difficulty)
health=health+potion_health
print(health)


print(round(2.8))
print("Math floor 2.8: ",math.floor(2.8))
print(math.ceil(2.8))
print(math.sin(math.pi/2))
print(math.sin(math.pi))
print(math.floor(math.sin(math.pi)))
print(math.cos(0))
print(math.asin(0))
print(math.acos(0))
print(math.hypot(3,4))
print(math.pow(2,3))
print(2**3)
print(math.exp(2))
print(math.log(math.e))
print(math.log10(1000))
print(math.log2(16))
print('John said to me,"I owe you 10 bucks"!!!!')
A="Part"
B=1
out="{}-{}".format(A,B)
print(out)
#ask your for name
name=input("What is your name?: ")
print(name)
#ask your for age
age=input("How old are you?: ")
print(age)
#ask user for city
city=input("Where do you live in?: ")
print(city)
#ask user what they enjoy
love=input("What do you love doing?:")
print(love)
#create output text
out="Your name is {} and you are {} years old. You live in {} and you love {}.".format(name,age,city,love)
#print output to screen
print(out)


#count text letter
out="BONYROY".count("O")
print(out)
out1="Happy Happy Day".count("Day")
print(out1)

x="happy BirThday"
print(x.lower())
print(x.upper())


