#Positional arguments (ordered values like 1, 2, 3).
'''
def add(*a):
        print(a)
        print(type(a))
        result=0
        for i in a:
                if type(i)==int or type(i)==float:
                        result=result+i
        print(result)
add(12,3,4,'codegnan','saketh',2.3)



#keyword variable length arguments -->we can pass wny number of keyword arguments, we will use the representation as **kwargs, data is stored in dictionary.

def admission(**kwargs):
        print(kwargs)
        print(type(kwargs))

admission(name='balaji',mobile=7416866586,email_id='akulabalaji@gmail.com')

details={'id_nos':[234,345,342],
         'names':['balaji','ganesh','ram'],
         'batches':['DA-06','DA-06','DA-06']
         }
admission(**details)
'''
def simple(*a,**b):
    print(a)
    print(b)
    result=0
    for i in a:
        if type(i)==int or type(i)==float:
            result=result+i
    print(result)
    for key,value in b.items():
        print(f"keys are {key}")
        print(f"values are {value}")

simple()
details={'id_nos':[234,345,342],
         'names':['balaji','ganesh','ram'],
         'batches':['DA-06','DA-06','DA-06']
         }
         
simple(1,'poll',2,3,name='sai',place='vizag',**details,)
