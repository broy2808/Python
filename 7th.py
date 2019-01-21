#packing and unpacking of variables

numbers=[1,2,3,4,5]
print(*numbers)#unpacking arguments indivisually for iterable data types
#So we can unpack any iterable data types before they go to function
print("abc")#normal
print(*"abc")#unpacked

def add(*numbers):#packing
     total=0
     for number in numbers:
         total=total+number
     return (total)
#packing is very useful when you don't know how many arguments your function expecting
print(add(1,2,3,4,5,6))#passing arguments

def about(name,age,likes):
    sentence="Meet {}! I am {} years old and I like {}.".format(name,age,likes)
    return sentence

dictionary={"name":"Bony","age":23,"likes":"Python"}
#one star for normal arguments
#2 star for keyword arguments like dictionary with key value pairs
print(about(**dictionary))#unpack

# this is exactly same as typing about(name="Ziyad",age=23,likes="Python")

def foo(**kwargs):#creating dictionary
    #very useful for packing down keyword arguments into dictionary and loop through them
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

print(foo(huda="female",bony="female",john="male"))
