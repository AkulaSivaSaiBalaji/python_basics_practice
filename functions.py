'''
def intro():
    #Intro to functions
    return "Ayya namaskaram"

print(intro())

def add(a,b):
    "simple ga kalapadam"
    return a+b

print(add(5,7))
print(add('my name is',' billa'))
print(add([1,2,3],[4,5,6]))
a,b=map(int,input("Enter nubers: ").split(' '))
print(add(a,b))
'''
def grocery(item=None,price=None):
    #keyword argument usage#
    print(f'Item is {item}')
    print(f'Price is {price}')

grocery('Bread',45)
grocery(price=55,item='cake')
grocery()
grocery('curd')