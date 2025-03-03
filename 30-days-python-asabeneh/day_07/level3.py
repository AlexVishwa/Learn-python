age = [22, 19, 24, 25, 26, 24, 25, 24]
set1=set(age)
# Output: {19, 22, 24, 25, 26}
print(len(set1))
# Output: 5
print('Length of list is more as it has repeated characters {}'.format(len(age)))

sentence="I am a teacher and I love to inspire and teach people."
sentence=sentence.replace('.','')#this helps to remove full stop at the last
listofwords=sentence.split(' ')
print(listofwords)
set2=set(listofwords)
print(set2)
print("Repeated words are {}".format(len(listofwords)-len(set2)))