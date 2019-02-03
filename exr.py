def lesser_of_two_evens(a,b):
    if ((a%2==0)and(b%2==0)):
        if a>b:
            return b
        else:
            return a
    else:
        if a>b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,5))


def animal(a):
    s = a.split(' ')
    x1=s[0]
    x2=s[1]
    if x1[0]==x2[0]:
        return True
    else:
        return False
print(animal('Levelheaded Liama'))
print(animal('Crazy Kangaroo'))


def twenty(x,y):
    if ((x==20)or(y==20)or(x+y==20)):
        return True
    else:
        return False
print(twenty(10,5))

def mac(text):
    s1=text[0:3]
    s2=text[3:]
    
    return s1.capitalize()+s2.capitalize()
print(mac('macdonald'))


def master(s):
    a=s.split()
    s=''
    y=len(a)-1
    for each in range(0,len(a)):
        s+=a[y]+' '
        y=y-1
        
    return s

print(master('I am home'))

def master2(s):
    a=s.split()
    s=a[::-1]
    return ' '.join(s)

print(master2('I am home'))

def almost_there(n):
    return (abs(100-n)<=10 or abs(200-n)<=10)
print(almost_there(150))

def has_33(nums):
    for x in range(0,len(nums)-1):
        if (nums[x]==3) and (nums[x+1]==3):
            return True
    return False
print("Has 33")
print(has_33([1, 3, 3]))
print(has_33([1, 3,1, 3]))
print(has_33([3,1, 3]))

def paper_doll(s1):
     final=''
     for x in s1:
         x1=x*3
         final+=x1
     return final

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

def blackjack(a,b,c):
    elev=0
    s=a+b+c
    if (s>21):
        if (a==11)or(b==11)or(c==11):
            s=s-10
    if s>21:
        return 'BUST'
    else:
        return s
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


def blackjack2(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

print(blackjack2(5,6,7))
print(blackjack2(9,9,9))
print(blackjack2(9,9,11))    

def summer_68(s1):
    final=0
    sixfound=0
    for x in range(0,len(s1)):
        if (sixfound==0)and(s1[x] !=6):
            final=final+s1[x]
        else:
            sixfound+=1
            if(s1[x]==9):
                sixfound=0
    return final

print(summer_68([1, 3, 5]))
print(summer_68([4, 5, 6, 7, 8, 9]))
print(summer_68([2, 1, 6, 9, 11]))     
                
def spy_game(nums):
    s=''
    for x in range(0,len(nums)):
        if (nums[x]==0)or(nums[x]==7):
            s=s+str(nums[x])
    if '007' in s:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([1,7,2,0,4,5,0,7]))

def prime(num):
    s=0
    li1=[]
    #check for 0 and 1
    if num<2:
        return 0
    # 2 o greater
    for x in range(2,num+1):
        if all(x%y!=0 for y in range(2,x)):
           s+=1
           li1.append(x)
    print(li1)
    return s
print(prime(100))














































    
        
