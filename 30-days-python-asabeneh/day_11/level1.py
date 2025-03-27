def sum(a,b):
    return a+b

print(sum(4,5.6)) #9.6

def aoc(r):
    return 3.14159265359 * (r**2)

print(aoc(2)) #12.56637061436

def sumOfMany(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sumOfMany(1,2,3,4,5,6,7,8,9,10))
# Output: 
# 55

a=['a','b','c','d','e','f','g','h','i','j']

def capitalize_list_items(a):
    return list(map(lambda x: x.upper(), a))
print(capitalize_list_items(a))

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def func1(a, item1):
    a.append(item1)
    return a
print(func1(a,'k'))

def func2(list, item):
    if(item in list):
        list.remove(item)
    return list
listnew=[2,45,68,34,23,56,78,90,12,34,56,78,90]
print(func2(listnew,56))
#Output:
# [2, 45, 68, 34, 23, 78, 90, 12, 34, 56, 78, 90]
def func13(num):
    sum=0
    for i in range(num):
        sum+=i
    return sum

print(func13(10))

#Output:
# 45

def func14(rang1):
    sum=0
    for i in range(rang1):
        if i%2==0:
            sum+=i
    return sum
print(func14(10))
#Output:
# 20

def func15(rang1):
    sum=0
    for i in range(rang1):
        if i%2!=0:
            sum+=i
    return sum
print(func15())

#Output:
# 25