'''
BMI scenario --> link with exception handling with usage of while

while <condition>:
    statements(s)...
    .....
'''
i=0
frineds={'name':[],'weight':[],'height':[],'BMI':[]}
while i<2:
    #now we are gonna link bmi case to it with exception handling
    i+=1
    try:
        weight = int(input("enter the weight in kgs:"))
        height = float(input("enter the height in feet:"))
        name=input("Enter name: ")
        if weight > 0 and height > 0:
            #print(weight,height)
            height=height*0.3048
            frineds["name"].append(name)
            frineds["weight"].append(weight)
            frineds["height"].append(height)
            bmi=weight/(height**2)
            if bmi<18.5 and bmi>0:
                print(f"BMI: {bmi} and you are Underweight")
                frineds["BMI"].append(f"Underweight: {bmi}")
            elif bmi>=18.5 and bmi<=24.9:
                print(f"BMI: {bmi} and you are Healthy")
                frineds["BMI"].append(f"Healthy: {bmi}")
            elif bmi>24.9 and bmi<=29.9:
                print(f"BMI: {bmi} and you are overweight")
                frineds["BMI"].append(f"overweight: {bmi}")
            elif bmi>29.9 and bmi<=35.9:
                print(f"BMI: {bmi} and you are Obbese")
                frineds["BMI"].append(f"obbese: {bmi}")
            else:
                print("⚰️")
                frineds["BMI"].append(f"Near Death Bed ⚰️: {bmi}")
            
        else:
            print("value of weight/height must be positive")
    except Exception as e:
        print(e)

print(frineds.keys(),frineds.values())
'''        
frineds["name"].append(name)
frineds["weight"].append(weight)
frineds["height"].append(height)
bmi=weight/(height**2)
if bmi<18.5 and bmi>0:
    print(f"BMI: {bmi} and you are Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print(f"BMI: {bmi} and you are Healthy")
elif bmi>24.9 and bmi<=29.9:
    print(f"BMI: {bmi} and you are overweight")
elif bmi>29.9 and bmi<=35.9:
    print(f"BMI: {bmi} and you are Obbese")
else:
    print("⚰️")
'''