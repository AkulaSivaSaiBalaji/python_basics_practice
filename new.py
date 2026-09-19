'''
batch=['sai','PFS-6','DA-6','balaji','karthik','ganesh','yashwanth']
print(batch[::2]) #striding: iterable.[start:stop:step]
print(batch[::3])
print(batch[1::2])
print(batch[1:5:2])
print(batch[-1:-5:-2])
print(batch[1:7:-2])
print(batch[7:1:-2])
batch.insert(3,['Pfs','Da','Jfs'])
print(batch)
batch[3][2]=batch[3][2].upper()
print(batch[3][2])
batch[3].append('AAA')
print(batch)

batch = ['sai','pfs-6','da-6','saketh','aksah','python','anil']


print(batch[2:6:3])# first 2:6 --> skip 2 elements
print(batch[1:7:-2])# in  this case u will recieve empty list
print(batch[-1:-4:-1])#in this case we come in reverse order
print(batch[-1:-4:-2])
#in this above case be careful while applying negative step count

#lets include tuple in above list(tuples are immutable)
batch.insert(2,("vizag","hyd","vijayawada"))
print(batch)
#print(len(batch))
#as we have a tuple inside a list

print(len(batch[2]))
print(batch[2][:2])
print(batch[2][1])#this string 'hyd' -->string
print(batch[2][::2])#returns ("vizag","vijayawada")
print(batch[2].index('hyd'))#tuple will have only count,index
#index --> first occurance
#count --> returns the count of objects
print(batch[2].count('codegnan'))#returns count as 0
#index will raise error,where as count will retutn 0

batch.insert(3,['pfs','da','jfs'])
print(batch)
#batch now let us apply some of list functions in above batch list
print(batch[3])
print(batch[3][1])
# to convert only jfs as upopercase -->
batch[3][2]= batch[3][2].upper()
print(batch[3][2])
#now we wanted to add new course in batch[3] position --> AAA
batch[3].append('AAA')
print(batch[3])
print(len(batch))
batch.remove('aksah')
print(batch)
#batch[2].remove('hyd') #doesnot work because tuple is immutable we cannot change or delete any item 
batch.clear()
print(batch)


details={}
print(len(details))
details['batch']=['PFS6']
print(details)
details['course']=['python']
print(details)
print(len(details))
details['students']=['sai','lahar']
print(details)
details.update({'branch':('hyd','vizag'),'subjects':{'python','apptitude','softskills'}})
print(details)
print(len(details))
print(details.keys())
print(details.values())
print(details.items())
details['batch'].append("DA-6")
details['batch'].extend(['JFS',"AAA"])
print(details)
print(len(details))
details['students'].extend(['Ganny','sarath','kartheek','yashwanth'])
print(details['students'])
details['subjects'].add('excel')
print(details['subjects'])#set is unique and unordered
''' 

