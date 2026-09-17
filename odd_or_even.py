number=int(input("Enter a number: "))
if number==0:
    print("Zero is neither even nor odd ")
else:
    if number<0 and number%2==0:
        print("Negative Even Number")
    elif number<0 and number%2!=0:
        print("Negative Odd Number")
    elif number>0 and number%2==0:
        print("Even Number")
    elif number>0 and number%2!=0:
        print("Odd Number")
