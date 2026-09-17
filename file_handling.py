'''notes=input("Enter file name: ")
lines=input("enter notes: ")

with open(notes,'w') as file:
    file.write(lines)

with open(notes,'r') as file:
    output=file.read()
    print(output)
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