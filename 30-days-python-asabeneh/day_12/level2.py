from random import randint
def hexcodegen(n):
    list1=['A','B','C','D','F','E']
    list2=['0','1','2','3','4','5','6','7','8','9']
    r=''
    for i in range(0,n):
        for j in range(0,3):
            r+=list1[randint(0,5)]+list2[randint(0,9)]
        print(r)
        r=''
    return r

# print(hexcodegen(5))
# f0f0f0

def list_of_rgb_colors(n):
    # i=int(input("Enter the number of colors"))
    list1=[]
    for j in range(n):
        r=f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'
        print(r)
        list1.append(r)
    return list1
# print(list_of_rgb_colors())

def generate_colors():
    # i=int()
    k,j=map(int, input("Enter the number of colors and hex colors").split())
    hexcodegen(k)
    list_of_rgb_colors(j)
generate_colors()
