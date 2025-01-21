# age=int(input("Enter your age"))
# if age<18 :
#     print("Wait for missing years")
# else:
#     print("Fit to drive")

my_age=int(input(print('My age \n')))
yours_age=int(input(print('Yours age \n')))
if (yours_age > my_age):
    if(yours_age - my_age == 1):
        print('you are just one year old')
    print(f'you are just{yours_age - my_age} year old')
elif (yours_age==my_age):
    print("we are of same age")
else:
    print('I am older than u')