'''
Functions : User defined functions, in-built functions, anonymus functions(lambda keyword), recursive function

anonymus function: nameless functions (helper functions ) we, define them by using lambda keyword
syntax: lambda arg(s): expression  
def area_of_rect(l,b):
    rect = lambda x,y : x * y
    return rect(l , b)
a = area_of_rect(7,4)
print(a)
'''


'''
same using anonymus function

area = lambda l ,b : l *b
print(area(7,4))

social media user login first name last name--> full name

fname,lname = map(str, input("Enter the name").split(','))
full_name = lambda fname,lname : fname.title().strip() + ' ' +lname.title().strip()
print(full_name(fname,lname)) 
'''


'''
#accessing input from user and find even or odd

n = int(input())
result = lambda n : 'even' if n % 2 == 0 else 'odd'
print(result)

names = ['yash','rocky','salaar','internationa']
name_ = lambda x: x in names# here membership operator always returns boolean values(True,False)
names_ = lambda x:len(x) in names# here membership operator always returns boolean values(True,False)
j = lambda x : len(x)
print(name_('rocky'))
print(names_('international'))


#filter(),map(),reduce()
#filter()-->when we want specified filtered result

data=[1,3,4,5,24,12,36,3]
new_data=list(filter(lambda x:x%2==0,data))
print(new_data)

def filter_even(*b):
    new_data=[]
    for i in b :
        if i%2==0:
            new_data.append(i)
    return(new_data)

data=[1,3,4,5,24,12,36,3]
print(filter_even(*data))

names=['saketh','Python','Akash','Ganesh','sarath']
new_name=list(filter(lambda i:len(i)>=6,names))
print(new_name)

#map()-->it will apply logic for each value (google maps)
lst=list(map(int,input("Enter the values").split(',')))
print(lst)
data=[1,3,5,7,-23]
final=list(map(lambda x,y:x+y, lst,data))
print(final)


#reduce --> functools
#reduce -->it will check for logic and make it to a single value
import functools
from functools import reduce
result=reduce(lambda x,y:x*y,[12,3,4,5,6])
print(result)
f=reduce(lambda x,y:x+y,[12,3,4,5,6])
print(f)


def mul(data):
    num=1
    for i in data:
        num*=i
    print(num)

data=[12,3,4,5,6]
mul(data)

def add(data):
    num=0
    for i in data:
        num+=i
    print(num)

data=[12,3,4,5,6]
add(data)


#recurrsive functions: A function calling itself

def fun():
    """doc string"""
    if base:
        return
    fun()
fun()

def test():
    """testing"""
    return test() #returns error since no stopping condition
print(test())

n=int(input("enter number: "))
def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "Input must be grater than 1"
    else:
        return n*fact(n-1)
print(fact(n))
import random
a=lambda : random.randint(1000,9999)
print(a())'''


a = set()
    # range(1000, 9999) generates numbers from 1000 to 9998
for i in range(1000, 9999): 
    a.add(str(i))
a=list(a)
print(int(a[143]))
