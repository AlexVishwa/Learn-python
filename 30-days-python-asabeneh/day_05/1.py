list1= []
list2=['Apple','Mango','Strawberry','Banana', 'Kela', 'Orange']
length_of_list=len(list2)
print(length_of_list)

print(list2[0])
print(list2[-1])

if(length_of_list%2 == 0):
    len1=length_of_list/2
    print(list2[int(len1)])
else:
    len2=length_of_list+1/2
    print(list2[int(len2)])

mixed_data_types=['Alex',31,'5\'8"', 'Unmarried']
print(mixed_data_types)

it_companies=['Facebook','Apple','Google','Microsoft','IBM','Oracle','Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])

print(it_companies[-1])
length_of_list=len(it_companies)
if(length_of_list%2 == 0):
    len1=length_of_list/2
    print(it_companies[int(len1)])
else:
    len2=(length_of_list+1)/2
    print(it_companies[int(len2)])


it_companies.append('VIOM')
print(it_companies)

length_of_list=len(it_companies)
if(length_of_list%2 == 0):
    len1=length_of_list/2
    it_companies[int(len1)]='New'
else:
    len2=(length_of_list+1)/2
    it_companies[int(len2)]='New'

print(it_companies)
list2=['#;']
it_companies.extend(list2)
print(it_companies)
if(it_companies[2]=='IBM'):
    print('IBM')
else:
    print(it_companies[2].upper())

for company in length_of_list:
    i=0
    it_companies[i]=company+'#;'
    i=i+1

for company in it_companies:
    print(company)
