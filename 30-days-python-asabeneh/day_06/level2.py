# level2 continued from level1
fruits=tuple()
fruits=('Apple','Guava','Pomegranate','Pineapple','Custard Apple')
veggies=tuple()
veggies=('Baigan','Ghiya','Petha','Chana','Hari matar')
animalprod=tuple()
animalprod=('Fish','Kebab','Rolls')
food_stuff_tp=animalprod+fruits+veggies
print(food_stuff_tp)
# Output:
# ('Fish', 'Kebab', 'Rolls', 'Apple', 'Guava', 'Pomegranate', 'Pineapple', 'Custard Apple', 'Baigan', 'Ghiya', 'Petha', 'Chana', 'Hari matar')
food_stuff_li=list(food_stuff_tp)
length=len(food_stuff_li)-1
print(food_stuff_li[int(length/2)])
#Output:
# Pineapple
print(food_stuff_li[0],food_stuff_li[1],food_stuff_li[-1],food_stuff_li[-2])
# Output:
# Fish Kebab Hari matar Chana
# del food_stuff_tp
# print(food_stuff_tp)
# Output:
# NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_li'?
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
try:
    print(nordic_countries.index('India'))
    # print('India' in nordic_countries)
# Works for tuple as well as list, in and not in
except ValueError:
    print("Doesn't exists")
# ValueError: tuple.index(x): x not in tuple