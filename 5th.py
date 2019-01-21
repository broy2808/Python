for number in range(1,5):
    print(number)

for number in [2,6,7,8,9]:
    print(number)

for number in "ABCD":
    print(number)

for number in range(1,6,2):
    print(number)


vowels=0
consonants=0

for letter in "BONYroy":
  if letter.lower() in "aeiou":
     vowels=vowels+1
  elif letter==" ":
     pass
  else:
      consonants=consonants+1

print("There are {} vowels. ".format(vowels))
print("There are {} consonants. ".format(consonants))


students={
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["Sara","Huda","Samantha","Emily","Elizabeth","Ann"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name.lower():
            print(name)

#list comprehension in one line
even=[x for x in range(1,101) if x%2==0]
print(even)


odd=[x for x in range(1,101) if x%2!=0]
print(odd)


#list of list creation through loop in one line
words=["the","quick","brown","fox","jumps","over","the","lazy","dog"]

ans=[[w.lower(),w.upper(),len(w)] for w in words]
print(ans)

#get sentence from user
original=input("Please enter a sentence. ").strip().lower()

# split sentence into words(create list of words through split)
words=original.split()

#loop through words and convert to pig latin
new_words=[]

#otherwise,move the first consonant cluster to end, and add "ay"
for x in words:
    #if starts with vowel, just add "yay"
     if x[0] in "aeiou":
       new_word=x+"yay"
       new_words.append(new_word)
     else:
          vowel_index=0
          for letter in x:
             if letter not in "aeiou":
                 vowel_index= vowel_index+1
             else:
                 break
          cons=x[:vowel_index]
          the_rest=x[vowel_index:]
          new_word=the_rest+cons+"ay"
          new_words.append(new_word)
    
#stick words back together
output=" ".join(new_words)

#output the final string
print(output)




































