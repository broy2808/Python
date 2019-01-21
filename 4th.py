#Tuple cannot be changed.So,immutable data type

our_tuple=(1,2,3,"A","B")
print(our_tuple)
#List and mutable and tuples are immutable
A=[1,2,4]
A=tuple(A)
print(A)

(C,D,E)=(1,2,3)#Tuple assignment
print(C)
print(D)
print(E)

#Dictionary-Key value pair storage
students={"Alice":25,"Bob":27,"Dan":21,"Emma":28}
# but this(he={ali:34}) will not work as he is been seen as a variable
print(students["Bob"])
#adding a value

students["Fred"]=29
print(students["Fred"])

#change a value
students["Bob"]=28
print(students["Bob"])

#delete fred
del students["Fred"]
print(students.keys())
#we cannot directly convert students.keys().We need to change it to list
print(list(students.values())[0:])
#dictionary does not have order.we can only access it by keys
print(students)
print(students.items())#all items

# dictionary list combine
students={
              "Alice":["ID0001",26,"A"],
              "Bob":["ID0002",28,"B"],
              "Dan":["ID0003",29,"C"],
              "Emma":["ID0004",25,"D"]
              }
print(students["Dan"])
print(students["Dan"][0])
print(students["Dan"][1:])

#dictionary of dictionary
students={
              "Alice":{"id":"ID0001","age":25,"grade":"A"},
              "Bob":{"id":"ID0002","age":25,"grade":"A+"},
              "Dan":{"id":"ID0003","age":27,"grade":"B"},
              "Emma":{"id":"ID0004","age":27,"grade":"A"}
              }


print(students["Dan"]["id"])
print(students["Emma"]["id"],students["Emma"]["age"])














