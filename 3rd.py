#List
our_list=[27,56,5,17,99]
print(our_list)

#List can have multiple data type inside them like int,string together
Jackson=["A","ROY","Hey",14,56,"Tr"]
print("Frontside :",Jackson[4])
print("Backside :",Jackson[-4])
print("Slice backward:",Jackson[-3::-1])

#List can have another list inside them
ourlist=[1,2,[3,4,5],6,7,4]
print("Print list inside list :",ourlist[2])
print("Print one element of list inside list :",ourlist[2][0])
print("Print last 2 elements of list inside list :",ourlist[2][1:])
print("Print 2 step elements of list inside list :",ourlist[2][0::2])



#Small project
known_users=["Alice","Bob","Claire","Bony","Dan","Lucifer","Chloe","Sayoni","Dimpi"]
print(len(known_users))

while True:
    print("Hi! I am the Security System here!!")
    name=input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!!.".format(name))
        remove=input("Would you like to be removed from the system (y/n)? ").lower()
        if remove=="y":
            known_users.remove(name)#remove don't remove duplicate values only removes 1st match
            print("{} removed!!!".format(name))
        else:
            print("Thanks for visiting!!!")

    else:
       print("Hmm I don't think I have met you {}".format(name))
       addme=input("Would you like to be added into the system (y/n)? ").lower()
       if addme=="y":
           known_users.append(name)
           print("Congrats!!!! you are added in the system {}. ".format(name))
       else:
           print("Thanks for visiting!!!")
    break

L=[1,3,67,87]
del L[2]
print(L)

L=L+[12,78]
print(L)
L=L+["ABC"]
print(L)
L=L+list("BRE")
print(L)
L=L+[[14,60,54]]
print(L)
L.append([30,32,45])
print(L)


K=[5,12,45,65]
K.insert(2,100)#insert 100 at index 2
print(K)
#insert whole list at index 2
K.insert(2,[10,20,30])
print(K)
#List are mutable and strings are immutable





