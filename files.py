#Sample windows file path for reading/writing file "C:\\Users\\Bony\\test.txt".Use double backslash for windows

#mode='r' is read only
#mode='w' is write only(will overwrite or create newfile)
#mode='a' is append only(will add on to files)
#mode='r+' is reading and writing
#mode='w+' is writing and reading(will overwrite or create newfile)
file = open("testfile.txt","w") #oldway.Need to close file manually by close()
file.write("Hello World\n") 
file.write("This is our new text file\n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.\n") 

file.close()

file1=open("testfile.txt","r")#oldway
print(file1.read())
file1.seek(0)#reset the cursor for reading to 0
print(file1.read())
file1.seek(0)
print(file1.readlines())#readline used for reading list objects

#modern file open.If we do this syntax we don't need to close() file manually.
with open("testfile.txt","r") as my_new_file:
    print(my_new_file.read())

with open("testfile.txt","a") as my_new_file:
    my_new_file.write('New file append')
   
with open("testfile.txt","r") as my_new_file:
    print(my_new_file.read())

list4=[5,4,3,2,1,6]
print(sorted(list4))
list4.sort()
print(list4)

d={"simple_key":"hello"}
print(d["simple_key"])
print(d.get("simple_key"))
print(d.values())

d={"k1":[{"nest_key":["this is deep",["hello"]]}]}
print(d["k1"][0]["nest_key"][1][0])
#we cannot sort a normal dictionary
#set do not allows duplicate values


#tuple unpacking
mylist=[(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist:
    print(a)
    print(b)

d={'k1':1,'k2':2,'k3':3}

for item in d.items():
    print(item)   

for key,value in d.items():
    print(key," ",value)

for value in d.values():
    print(value)
#break=breaks out of the current closest enclosing loop
#continue=Goes to the top of the current closest enclosing loop
#pass: Does nothing at all.

#Enumerate-Index count automatically formatted like tuple
word="HELLO BONY"

for item in enumerate(word):
    print(item)
   
for index,letter in enumerate(word):
    print(index)
    print(letter)

#zip=zip together 2 lists and pair up items from 2 lists and produce tuple
    
mylist1=[1,2,3]
mylist2=['a','d','e']
for item in zip(mylist1,mylist2):
    print(item)

for item in list(zip(mylist1,mylist2)):
    print(item)

mylist=[20,56,65,21,3,4,7]
print(min(mylist))
print(max(mylist))

from statistics import mean
from random import shuffle
from random import choices
mylist=[1,2,3] #shuffle does not returns anything only shuffles the list
shuffle(mylist)
print(mylist)

te=choices(['red', 'black', 'green'], [1,2,10], k=6)
print(te)


from random import randint
print(randint(0,100))


li="Hello"
print([x for x in li if x=="l"])#list comprehension
print([num**2 for num in range(0,11)])

#if else statement in list comprehension.Not recommendad
result=['{} EVEN'.format(x) if x%2==0 else '{} ODD'.format(x) for x in range(0,11)]

print(result)
#double for loop with list comprehension
result=[x*y for x in [4,5,7] for y in [1,10,100]]
print(result)

st='Print every word in this sentence'

li=st.split()
for x in li:
    if len(x)%2==0:
        print(x,' even!')

for x in range(0,100):
    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%5==0:
        print('Buzz')
    elif x%3==0:
        print('Fizz')
    else:
        print(x)
















