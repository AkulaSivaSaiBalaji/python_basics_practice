'''notes=input("Enter file name: ")
lines=input("enter notes: ")

with open(notes,'w') as file:
    file.write(lines)

with open(notes,'r') as file:
    output=file.read()
    print(output)
'''
'''
first,second=map(int,input("enter the values :").split(","))
print("======CALCULACTOR======")
print()
print("This Calculactor supports (+,-,/,*)")
print()
print(f"Addition is: {first+second}")
print(f"Subraction is : {first-second}")
print(f"division: {first/second}")
print(f"multiplication is: {first*second}")
'''
#with open('secret.txt','r') as file:
    #print(file.read())
'''
file=open('secret.txt','r')
print(file.read())
print(file.readline())
'''


#file=open('saketh.txt','w')
#file.write("Saketh sir chala manchivaru")#
#file.close()
'''
with open('saketh.txt','w') as file:
    file.write("Improving my python")
'''
'''
data =['Codegnan','Python','vizag','DA']
with open('qw.txt','w') as file:
    #file.write(data) # this wil give error since write will accpect only strings 
    file.writelines(data) #this can directly insert data into file from list
'''

#''a mode will create a new file, if file already exists it will append the data at last without overriding like that write mode
#with open('append.txt','a') as file:
#   file.write("\nMy name is balaji and ganny is artist")

with open('append.txt','+r') as file:
    print(file.read())
    file.write("job ravali")