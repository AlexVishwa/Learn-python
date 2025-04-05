s='30 days'
t=' of'
u=' python'
r=s+t+u
print(r)

company="Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print("Title"+company.title())

print("Swapcase :"+company.swapcase())

print(company[0:6])

# print(company.index('coding'))

print(company.replace('Coding', 'fun')) #This is used in Level20

print(company.split(' '))

companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(','))

print(companies[0])

print(len(company.split(' ')))
#str=company.split(' ')

#print(str[1])

print(company[10])

quote= 'Python For Everyone'

str2= company.split(' ')

for str in str2:
    print(str[0])


quote= 'Python For Everyone'

print(quote.find('P'))

stmt='Coding For All'

print(stmt.find('F'))

print(stmt.rfind('o'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

sentence='You cannot end a sentence with because because because is a conjunction'
str3='because because because'
occ=sentence.index('because')
length_of_substr=len(str3)
print(occ)
print(length_of_substr)
print(sentence[occ:(occ+length_of_substr)])

str='Coding For All'
print(str.startswith('Coding'))
print(str.endswith('coding'))

str='   Coding For All      '
print(f'{str} after stripping {str}')
# print(str.rtrim)

str='I am enjoying this challenge.\nI just wonder what is next.'
print(str)

fields=['Name','Age','Class','Designation']
values=['Alex','25','6','Indep']
print(f'{fields[0]}\t{fields[1]}\t{fields[2]}\t{fields[3]}')
print(f'{values[0]}\t{values[1]}\t{values[2]}\t{values[3]}')

radius=10
Area= 3.14*(radius**2)
print(f'Radius = {radius}')
print(f'Area = 3.14 * 2 ** {radius}')
print(f'The area of a circle with radius {radius} is {Area} meters square.')

a=8
b=6
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')