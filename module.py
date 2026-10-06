""" A module is a python file (.py) containing usable logic"""
import importing_file
print(dir(importing_file))
print(type(importing_file.data))
print(type(importing_file.details))

#always first check the type

print(importing_file.data)
importing_file.details("nasty",'town')

from importing_file import *
print(data)
data['marks']=[45,64,89,79]
print(data)
print(importing_file.__doc__)
print(__doc__)
print(id(data))
print(id(importing_file.data))
print(id(importing_file.details))
details("balaji",'hyd')