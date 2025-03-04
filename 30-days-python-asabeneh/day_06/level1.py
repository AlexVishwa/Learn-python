tuple1=tuple()
tuple1=('Shubham','Mansi','Aastha','Anshita')
bro=('Shubham','Deepak')
sis=('Aastha','Anjali','Mansi')
siblings=bro+sis
print(siblings)
length=len(siblings)
print(f'("My siblings"= {length})')
family_members=list(siblings)
family_members.extend(['Shri Anand Prakash','Shrimati Laxmi'])
family_members=tuple(family_members)
print(f'Family={family_members}')
############Level2###################
family_members=list(family_members)
parents=family_members[5:7]
siblings=family_members[0:5]
print(siblings)
print(parents)
