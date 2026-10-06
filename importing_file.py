'''
Functions-->user defined functions,built-in-functions,anonymous functions
(lambda keyword),recursive function-->procedure oriented programming

modules-->A python file containing variables,functions and classes,object

Userdefined modules,built-in modules,available modules(pypi)'''

def details(name,place):
    """Details to be stored"""
    print(f"name is {name}")
    print(f"place is {place}")

#details("balaji","vizag")

data={'ids':[12,32,43,23],
      'names':['saketh','Akash','ganesh','yashwanth'],
      'batches':['PFS','JFS','DA','AAA']}

if __name__=='__main__':
    details("saketh",'codegnan')
    print(data)

print(__name__)
if __name__=='importing_file':
    print("imported file")


print(id(data))
print(id(details))
details("yashwanth",'vizag')