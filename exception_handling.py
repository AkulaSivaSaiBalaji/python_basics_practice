notes=input("Enter file name: ")
lines=input("enter notes: ")

with open(notes,'w') as file:
    file.write(lines)

with open(notes,'r') as file:
    output=file.read()
    print(output)