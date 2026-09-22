'''
for i in range(3):#0,1,2
    for j in range(2):#0,1
        print(f"i={i} j={j}")

for i in range(3):#0,1,2
    for j in range(3):#0,1,2
        print(f"i={i} j={j}")
'''
'''
for i in range(3):#0,1,2
    for j in range(3):#0,1,2
        print(i,j,end=' ')# here end will print every result for every loop in one line
        print("python",end=' ')
    print("codegnan",end=' ')
    print()
'''
'''
for i in range(2):#0,1
    for j in range(i):#i=0 loop not executes for i=1 only 
        print(i,j)
'''
'''
for i in range(3):#0,1,2
    for j in range(i+1):#i=0+1,i=1+1,
        print(i,j)
'''
'''
for i in range(4):
    for j in range(i-1):#i-1=-1,i-1=0,
        print(i,j)
'''
'''
for i in range(3):
    for j in range(4):
        print('*',end=' ')
    print()
'''
'''
for i in range(3):
    for j in range(4):
        print(j+1,end=' ')
    print()
'''
'''
for i in range(3):
    for j in range(3):
        print('*',end=' ')
        if j==(i+1)/2:
            print(' ',end='')
    print()
'''


'''
for i in range(4):
    for j in range(4):
        print(i+1,end=' ')
    print()
'''
'''
c=0
for i in range(3):#0,1,2
    for j in range(3):#0,1,2
        c+=1
        if c%2!=0:
            print(c,end=' ')
        else:
            print(0,end=' ')
    print()
'''
'''
for i in range(3):
    for j in range(3):
        print(chr(65+j),end=' ')
    print()
'''
'''
rows=5
for i in range(1,rows+1):
    for j in range(rows-1):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
'''
'''
rows=5
c=0
for i in range(rows-1):
    for j in range(i+1):
        print(chr(65+c),end=' ')
        c+=1
    print()
'''
'''
rows=5
for i in range(rows-1):
    for j in range(i+1):
        print(i,end=' ')
    print()
'''
'''
rows=5
for i in range(rows-1):
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()
'''


for i in range(5):
    for j in range(5-i):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i-1):
        print("*",end=' ')
    print()

for i in range(4):

    for j in range(i+2):
            print(" ",end=' ')
    for j in range(3-i):
            print("*",end=' ')
    for j in range(2-i):
            print("*",end=' ')
    print()
