it_companies=['Facebook','Apple','Google','Microsoft','IBM','Oracle','Amazon']

set1= set(it_companies)
length_of_set=len(set1)

set1.add('Twitter')

set2={'Viom','Keymouse','Mouse'}
set3=set1.union(set2)
print(set3)

set1.remove('Twitter')

set1.discard('Codebrew')
