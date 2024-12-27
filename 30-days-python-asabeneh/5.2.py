# syntax
st = {'item1', 'item2', 'item3', 'item4'} #set
#st[0]='item0' 
#Error- TypeError: 'set' object does not support item assignment

st.add('item5')
# print(st(2)) #set is not ordered
#TypeError: 'set' object is not callable


st.remove('item5') #remove a particular item
print(st) #{'item4', 'item1', 'item3', 'item2'}
#item5 is added and then removed and the original set is printed

st.update(['item6','item7','item8']) 
print(st)#Output:{'item4', 'item8', 'item7', 'item1', 'item6', 'item3', 'item2'}
#as we can see the code runs the items to be added


# st.clear()
# print(st) #Output: set()

# del st
# print(st) # Output: NameError: name 'st' is not defined. Did you mean: 'set'?
#print("hello")

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
lst = set(lst)  # {'item2', 'item4', 'item1', 'item3'}
type(lst) #Output:
print(lst) 