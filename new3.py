a = 5
b = 3
c = 10
if a > b:
 print("a greater than b")
 if a > c:
  print("a is the greatest")
 else:
  print("c is the greatest")
else:
 print("b greater than a")
 if b > c :
   print("b is the greatest")
 else:
   print("c is the greatest")
s= "Hello"
print(s[0:4])
print(s[:1]+s[1:])
#List
colors =['red','blue','purple']
furniture =['Bed','Desk','Chair']
print(colors[0])
print (colors[0:3])
print (colors[1],colors[2])
print (furniture[2])
print (colors+furniture)
fur1=furniture
print (fur1[2])
numberss=[1,2,3,4]
print (numberss[1])
sum=0
for name in numberss:
 sum=sum+name
print ("Sum :" + str(sum))
for name in furniture:
 print (name)
if 'Bed' in furniture:
    print ("I need a Bed")
else:
    print ("You don't have a Bed")
for i in range(100,105):
 print (i)
a = [5, 1, 4, 3,10,89]
print (sorted(a))
print (sorted(a,reverse=True))
#Sorting different method
list=['aa','cc','bb']
list.sort()
print (list)
strs = ['ccc', 'aaaa', 'd', 'BB']
print (sorted(strs))
print (sorted(strs, key=len))
print (sorted(strs, key=len,reverse=True))
print (sorted(strs, key=str.upper)+sorted(strs, key=str.lower))
strs = ['xc', 'zb', 'yd' ,'wa']
def myFn(strs):
 return strs[-1]
print (sorted(strs,key=myFn))
#Tuple---Use () brackets
tuple1=(1,89,'Hello')
print (tuple1)
print (tuple1[2])
print (tuple1[0:3])
print (len(tuple1))
#tuple[2] = 'bye'#tuple don't allow item assignment.you need to create new tuple
#print tuple
tuple1 = (1, 2, 'bye')  ## this works
print (tuple1)
tup=(178)
tup=(178,)#I don't know why we are putting comma,it works without comma too
print (tup)
#comprehensive list
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]
print (squares)
small =[n for n in nums if n < 2]
print (small)
strs = ['hello', 'and', 'goodbye','bony']
shouting = [ s.upper() + '!!!' for s in strs ]
print (shouting)
#Dictionary---Represented by Curly brackets
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print (dict)
print (dict['a'])
dict ['a']='6'
print (dict['a'])
print (dict.get('z'))
## Note that the keys are in a random order.
for key in dict: print (key)
## Exactly the same as above
for key in dict.keys(): print (key)
## Get the .keys() list:
print (dict.keys())
print (dict.values())
## accessing each key/value
for key in sorted(dict.keys()):
 print (key, dict[key])
## .items() is the dict expressed as (key, value) tuples
print (dict.items() )
##Hash
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash
print (s)
##Del---The "del" operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined.
##Del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.
var = 6
del var  # var no more!
list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print (list)      ## ['b']

##Del Dictionary
Dict1={'a1':'Bony','d1':'Dimpi','s1':'Sayoni','o1':'Odd'}
print (Dict1)
print (Dict1.keys())

del Dict1['o1']
print (Dict1)

##function
def printme( str ):
  #This prints a passed string into this function"
  print (str)
  return
# Now you can call printme function
printme ("I'm first call to user defined function!")
##Pass by reference vs value
##All parameters (arguments) in the Python language are passed by reference.



L=['S','E','Q','U','E','N','C','E']
L1=[]
n=len(L)
while len(L)>0:
  max=len(L)
  min=0
  for i in range(0,max):
      if L[i]<L[min]:
        min=i
  print (L)
  temp= L[min]
  L1.insert(len(L1),temp)
  del L[min]
print (L1)


