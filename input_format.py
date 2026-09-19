#usage of %d,%f,%s
'''
price=45.3;grade="A";stock=15
print("%d"%price)#%d used to formart any type of numbers into int format
print("%f"%price)#%f used to pirnt float numbers will all decimal values
print("%.f"%price) #%.f will remove all decimal values and print only number
print("%.1f"%price)#%.1f will allow one decimal value after number
print("%s"%grade)

#find area of a circle radius is 3.5cm,round offthe area to 2 decimals values:

radius,pi=3.5,3.1416
area_of_circle=(radius**2)*pi
print("Area of circle is: %.2f"%area_of_circle)

#f-string

name="Balaji";status="single"
print(f"{name} is {status}")
'''

#control block statements
details={
    'name':[],
    'weight':[],
    'height':[]
}
for i in range(1):
    print("Select Units to represent your BMI: ")
    print()
    print("1: weight:KG and height:feet")
    print("2: weight:grams and height:meters")
    print("3 weight:pounds and height: centimeters")
    user_choice=int(input("Enter your choice(1 or 2 or 3) "))
    if user_choice==1 and user_choice>0:
        weight=float(input("Enter the weight: "))
        height=float(input("enter your height: "))
        name=input("Enter your name")
        details["height"].append(height)
        details["weight"].append(weight)
        details["name"].append(name)
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
    elif user_choice==2 and user_choice>0:
        weight=float(input("Enter the weight: "))
        height=float(input("enter your height: "))
        name=input("Enter your name: ")
        details["height"].append(height)
        details["weight"].append(weight)
        details["name"].append(name)
        weight=weight*1000
        height=height*0.3048
        bmi=weight/((height**2)*1000)
        print(bmi)
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

    elif user_choice==3 and user_choice>0:
        weight=float(input("Enter the weight: "))
        height=float(input("enter your height: "))
        inches =float(input("Enter your height (inches): "))
        weight=weight*2.20462
        height_in=height*12+inches
        bmi=weight/((height_in**2)*703)
        name=input("Enter your name: ")
        details["height"].append(height_in)
        details["weight"].append(weight)
        details["name"].append(name)
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

    else:
        print("Invalid Choice")

print(details)
