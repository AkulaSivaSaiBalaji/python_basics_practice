'''price_of_product=int(input("Enter product price: "))
discount=int(input("Enter your discount percentage: "))
discount=discount/100
gst=0.18

final_price = (price_of_product-(price_of_product*discount)) + (price_of_product*gst)
print(f"final_price is : {final_price}")
'''

'''prices=[15000,2000,13000,25000,35000]
final_prices=[]
for i in range(len(prices)):
    if prices[i-1]>5000 and prices[i-1]<=15000:
        prices[i-1]=prices[i-1]-(prices[i-1]*10/100)
        final_prices.append(prices[i-1])
    elif prices[i-1]>5000 and prices[i-1]>20000:
        prices[i-1]=prices[i-1]-(prices[i-1]*15/100)
        final_prices.append(prices[i-1])
    elif prices[i-1]<5000:
        final_prices.append(prices[i-1])
print(final_prices)'''

'''
students=[]
for i in range(3):
    marks=int(input("Enter marks: "))
    students.append(marks)
students.insert(0,90)
print(f"added 90 at first position: {students}")
extended_num=[75,85]
print(students)
students.extend(extended_num)
print(students)
if 75 in students:
    students.remove(75)
print(students)
popped_mark=students.pop()
print(f"popped_mark: {popped_mark}")
print(f"final list: {students} and it's length {len(students)}")
'''
'''
numbers = [20, 10, 30, 20, 40, 20] 
numbers.sort()
print(f"sorted list: {numbers}")
numbers.reverse()
print(f"descending order list: {numbers}")
search=int(input("enter a number to search in the list :"))
if search in numbers:
    print(f"number of occurances of that number is {numbers.count(search)}")
else:
    print("number not in list !!")
print(f"smallest value :{min(numbers)} \nlargest value : {max(numbers)} \ntotal sum of the numbers in list is : {sum(numbers)}")
'''
'''
numbers = [10, 15, 20, 25, 30, 35] 
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    elif num%2!=0:
        odd.append(num)
print(f"even list: {even}")
print(f"odd list: {odd}")
first_three=numbers[0:3]
last_three=numbers[3:6] #last_three=numbers[:-3]
print(f"first_three: {first_three}\nlast_three: {last_three}")
copy_numbers=numbers.copy()
numbers.clear()
print(f"copied list :{copy_numbers}\noriginal list :{numbers}")
'''

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
names=set(names)
print(f"removed duplicates: {names}")
names.add("Meera")
print(f"added meera: {names}")
added_names=["Arun","Priya"]
names.update(added_names)
print(names)
if  "John" in names:
    names.remove("John")
    print(names)
names.discard("David")
for name in names:
    count=0
    if name in names:
        count=count+1
    if count==1:
        print(name)
        
        