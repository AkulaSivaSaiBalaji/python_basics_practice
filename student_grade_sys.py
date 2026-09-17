marks=int(input("Enter student's marks:"))
if marks>0 and marks<100:
    if marks>=90:
        print("Grade: A")
        print("Remark: Outstanding")
    elif marks<90 and marks>=80:
        print("Grade: B")
        print("Remark: Excellent!")
    elif marks<80 and marks>=70:
        print("Grade: C")
        print("Remark: Good")
    elif marks<70 and marks>=60:
        print("Grade: D")
        print("Remark: Fair, needs improvement")
    elif marks<60 and marks>=50:
        print("Grade: E")
        print("Remark: Poor, needs serious improvement")
    else:
        print("Grade: F")
        print("Remark: Failed, needs to reappear")
else:
    print("Invalid marks entered")