# import multiprocessing from mp

# def __init__:

def is_prime(num):
    if(num==2):
        print("Prime Number")
    elif(num):
        for i in range(2,num):
            if(num%i==0):
                print("Not Prime Number")
                break
        else:
            print("Prime Number")

# is_prime(20000000000000000000000000000000000000000000000000456678977777987777777777777779466666666666666666666666333333333333333333333333333333333333333333335714389)

def check_list(list1):
    s1=set(list1)
    l1=len(list1)
    l2=len(s1)
    if(l1==l2):
        print("list is unique")
    else:
        print("list ain't unique")

# check_list([1,2,3,3,4,5,6,7,8,9,10])

def checkdt(list1):
    for i in range(len(list1)-1):
        a=type(list1[i])
        if(a==type(list1[i+1])):
            if(i==len(list1)-1):
                print("All elements are of same type")
            pass
        else:
            print("All elements are not of same type")
            break
# checkdt([1,2,3,'alex'])
    
def varname():
    var = input("Enter the variable name:\n")
    if var[0].isnumeric():  # Check if the first character is a number
        print("Variable name is invalid")
        return
    for char in var:  # Iterate through each character in the variable name
        if not (char.isalnum() or char == '_'):  # Only alphanumeric and underscore are valid
            print("Variable name is invalid")
            return
    print("Variable name is valid")

varname()