#lambda,map,filter


#map-map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

def square(num):
    return num**2
my_nums = [1,2,3,4,5]
print(list(map(square,my_nums)))#while using map you do not need to pass () only pass function name,rest will be done my map itself

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']

print(list(map(splicer,mynames)))


#filter-filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

def check_even(num):
    return num % 2 == 0

nums = [0,1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even,nums)))

#lambda expression
'''
One of Pythons most useful (and for beginners, confusing) tools is the
lambda expression. lambda expressions allow us to create "anonymous"
functions. This basically means we can quickly make ad-hoc functions
without needing to properly define a function using def.

lambda's body is a single expression, not a block of statements.
'''


#we can simplify the square function defined earlier

def square(num): return num**2
#This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:

lambda num: num ** 2

'''
So why would use this? Many function calls need a function passed in,
such as map and filter. Often you only need to use the function you are
passing in once, so instead of formally defining it, you just use the
lambda expression. Let's repeat some of the examples from above
with a lambda expression
'''
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda n: n % 2 == 0,nums)))

#Lambda expression for grabbing the first character of a string:
first=(lambda s: s[0])
print(first('Bony'))

rev=(lambda s: s[::-1])
#Lambda expression for reversing a string:
print(rev('Bony'))


#note that not every function can be translated into a lambda expression.

















