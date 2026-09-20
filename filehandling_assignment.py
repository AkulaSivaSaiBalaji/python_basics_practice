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

'''
with open('inventory.txt','a') as file:
    try:
        for i in range(3):
            product_name=input("Enter product name: ")
            quantity=input("Enter Quantity: ")
            copy_qnty=int(quantity)
            if copy_qnty>=0:
                file.write(';'+product_name+',')
                file.write(quantity)
            else:
                print("enter quantity grater than 1 !!")
    except ValueError:
        print("invalid values entered")

try:
    with open('inventory.txt','r') as file:
        inv=file.read().split(';')
        print()
        print("Current Inventory: ")
        search=[]
        for items in inv:
            print(items.replace(',',' - '))
            search.append(items)
            search.append(items.lower())
            search.append(items.upper())
        print()
        search_item=input("Enter Item to search in inventory: ")
        lower_search_item=search_item.lower()
        upper_search_item=search_item.upper()
        for i in search:
            if search_item in i or lower_search_item in i or upper_search_item in i:
                print(search_item+" is available.")
                print(i.replace(',',': '))
                break
except FileNotFoundError:
    print("unable to find the file")
'''

try:
    with open('students.txt','r') as file:
        passed_count=0
        failed_count=0
        total_passed_marks=0
        total_failed_marks=0
        for record in file.readlines():      
            details=record.split(",")
            student_name=details[0]
            try:
                marks=int(details[1].strip())
                if marks>=50:
                    print(student_name," - ",marks,' - Pass') 
                    passed_count+=1
                    total_passed_marks=total_passed_marks+marks
                else:
                    failed_count+=1
                    total_failed_marks=total_failed_marks+marks
                    print(student_name," - ",marks,' - Fail')
            except ValueError:
                 print(f"invalid marks for {student_name}")
                 print()
        sum=total_passed_marks+total_failed_marks
        count=passed_count+failed_count
        avg_marks=sum/count
        print("-------------------------") 
        print("Result Summary")
        print("-------------------------")
        print(f"Passed Students :{passed_count}")
        print(f"Failed Students :{failed_count}")
        print(f"Avarage Mark :{avg_marks}")
except FileNotFoundError:
    print("file not found")
