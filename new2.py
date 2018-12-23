import itertools

print("Hello Bony")
def is_palindrome(word):
    i=0
    j=len(word)-1
    while i<j:
     print (i,j)
     if word[i] != word[j]:
       return False
     #else:
       #return True
     i=i+1
     j=j-1
     
print (is_palindrome("madyam"))

sum1 =0
set1=[]
#min1=set1[0]
for x in set1:
 sum1=sum1+x
 #if min1 > x:
  #min1=x
print (sum1)


def contains_zero(S):
  for x in S:
   if x == 0:
    return True
  return False
S=[8,0,9]
print (contains_zero(S))

def keep_positives(S):
 if len(S) == 0:
  return 0
 else:
  result = []
  for x in S:
    if x > 0:
     result.append(x)
    if len(result)== 0:
     return 0
  return result
  
S=[-0.5,-7,-7,0]
print (keep_positives(S))

def keep_positives(S):
 if len(S) == 0:
  return 0
 else:
  result = []
  for x in S:
    if x > 0:
     result.append(x)
  return result
  
S=[0.5,7,-7,0]
print (keep_positives(S))


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print (newlist)

other=['abe',99.90,'edy']
other1=[789,'yut','qsv']
other3=[]
print (other+other1+other3)


'''
def chained(sequences):
    return itertools.chain.from_iterable(sequences)
sequences=['bony','99.90','dimpi']
print chained(sequences)'''

def keep_positives(S):
 result = []
 for x in S:
    if x > 0:
     result.append(x)
 return result
S=[]
print (keep_positives(S))

a=[2,7,8,91]
def odd_even(list1):
  result=[]
  for x in a:
    if((x%2)==0):
      s=str(x)+" is Even";
      result.append(s)
    else:
      s=str(x)+" is Odd";
      result.append(s)
  return result
print(odd_even(a))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_wout_dup(list1,list2):
    s=[]
    s=set(list1).intersection(set(list2))
    return s
print (list_wout_dup(a,b))

def fibo(a):
  x=[None]*3
  x[0]=0
  x[1]=1
  for i in range(2,a+1):
   x[2]=x[0]+x[1]
   x[0]=x[1]
   x[1]=x[2]
  return x[2]

print(fibo(7))
  
        


