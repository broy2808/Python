def add(x,y):
    return (x+y)

print(add(5,10))


def rev(text):
    return text[::-1]

print(rev("pen"))
print(rev([1,2,3,4]))
print(rev("1234"))

a=250

def f1():
    global a#rewrite global variable global a=100 will not work
    a=100
    print(a)

def f2():
    a=50
    print(a)

f1()
f2()
print(a)

#in list we can change information by changing little bit of it
a=[1,2,3]

def f1():
    a[0]=5#only one value changed
    print(a)

def f2():
    a=50
    print(a)

f1()
f2()
print(a)



#keyword arguments & default parameters

def about(name,age,likes):
    sentence="Meet {}! They are {} years old and they like {}.".format(name,age,likes)
    return sentence

print(about("Bony",27,"Python"))#positional arguments
print(about(age=23,name="Jack",likes="Python"))#keyword arguments

def about(name,age,likes="Python"):#parameters with default value have to come last
    sentence="Meet {}! They are {} years old and they like {}.".format(name,age,likes)
    return sentence


print(about("Bony",27))#as default value provided for "likes" parameter.We can skip to pass it while calling function and it will take default value
print(about("Bony",27,"Biriyani"))

















