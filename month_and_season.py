month_number=int(input("Enter Month Number: "))
if month_number<1 or month_number>12:
    print("Invalid month entered")
else:
    if month_number==12 or month_number==1 or month_number==2:
        print("Season: Winter")
    elif month_number==3 or month_number==4 or month_number==5:
        print("Season: Spring")
    elif month_number==6 or month_number==7 or month_number==8:
        print("Season: Summer")
    elif month_number==9 or month_number==10 or month_number==11:
        print("Season: Autumn")