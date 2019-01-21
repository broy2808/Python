films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters":[12, 5]
    }

while True:
    choice=input("What film you want to watch? ").strip().title()
    if choice in films:
        age=int(input("How old are you ?: ").strip())
        if age >= films[choice][0]:#check age
          if films[choice][1]>0:
              print("Enjoy the film.")
              films[choice][1]=films[choice][1]-1
          else:
              print("Sorry,we are sold out!")
        else:
          print("You are too young to watch the film!!")
        
    else:
        print("We don't have that film!!!")
    break

num=1

while num <=10:
    print(num)
    num=num+1

from random import choice
#import random
questions = ["Why is the sky blue?: ", "Why is there a face on the moon?: ",
                     "Where are all the dinosaurs: ","Why is the apple red?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "ok":
    answer = input("why?: ").strip().lower()

print("Oh... Okay")
