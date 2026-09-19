'''
with open('marks.txt','w') as file:
    try: 
        for i in range(5):
            marks=input("Enter marks: ")
            copy_marks=int(marks)
            if copy_marks>=0 and copy_marks<=100:
                file.write(marks+'\n')
                print("Marks Saved sucessfully")
            else:
                print("Enter marks between 0-100")
    except ValueError as e:
        print(e)

with open('marks.txt','r') as file:
    print(file.read())
'''

'''
with open('expense.txt', 'w') as file:
    for i in range(5):
        try:
            expense_amount = input(f"Enter expense amount {i+1}: ")
            copy_expense_amount = float(expense_amount)

            if copy_expense_amount >= 0:
                file.write(expense_amount + '\n')
            else:
                print("Enter expense >= 0")

        except ValueError:
            print("Invalid expense, please enter a number")

total_expense=0
with open('expense.txt', 'r') as file:
    print("Expenses:")

    expenses = file.readlines()
    for expense in expenses:
        print(expense.strip())
        total_expense += float(expense)
    print("Total expenses:", total_expense)
'''

'''
with open('attendance','w') as file:
    try:
        for i in range(5):
            stu_name=input("Enter Student Name: ")
            stu_attdedance=input("Enter attendance P - present and A - absent:  ")
            if "P" or "A" in stu_attdedance:
                file.write(stu_name)
                file.write(stu_attdedance+' ')
            else :
                print("Invalid attendance status")
    except FileNotFoundError as e:
        print("File does not exist")

with open('attendance','r') as file:
    att=file.read().split()
    print()
    print("Present Students: ")
    for i in att:
        if 'P' in i:
            print(i.replace('P',''))
'''

