def negative_integers():
    list1=[-4,-3,-2,-1,0,2,4,6]

    list2=[i for i in list1 if i<=0]

    list3=[i for i in list1 if i==0]

    return list2

def fourD_lists():
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    list1=[item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
    return list1
# print(flatten())

def series():
    list1=[
        (item**1,item**0,item**1, item**2, item**3, item**4, item**5)
        for item in range(11) 
        ]
    return list1
# print(series())

def formatted_country():
    countries=[
        [
            ("Finland", "Helsinki"),
            ("Sweden", "Stockholm"),
            ("Norway", "Oslo")
        ]
    ]
    list=[
        [country,country[0:3],capital]
        for outer in countries
        # for inner in outer
        for (country,capital) in outer
            ]
    return list
# print(formatted_country())
#TypeError: 'str' object is not callable

def list_of_dictionaries():
    countries=[
        [
            ("Finland", "Helsinki"),
            ("Sweden", "Stockholm"),
            ("Norway", "Oslo")
        ]
    ]
    lists=[
        {"country":country.upper(),
         "city":capital.upper()
         }
         for inner in countries
         for (country,capital) in inner
         ]
    return lists
# print(list_of_dictionaries())
def concatenation():
    names=[
        [
            ("Asabeneh", "Yetayeh"),
            ("David", "Smith"),
            ("Donald", "Trump")
        ]
    ]
    listnew=[
        first+''+last
        for outer in names
        for first,last in outer
    ]
    return listnew
# print(concatenation())
y= lambda m,x,c: m*x+c