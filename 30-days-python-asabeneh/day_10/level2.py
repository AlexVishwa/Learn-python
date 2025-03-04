# import '..\day_01\1.py'
sum=0
for i in range(101):
    sum= sum+ i

print(f"The sum of first 100 numbers is{sum}")

sum=0
for i in range(101):
    if(i%2!=0):
        sum=sum+i
print(f"The sum of odd numbers{sum}")
sum=0
for i in range(101):
    if(i%2==0):
        sum=sum+i
print(f"The sum of even numbers {sum}")
#Output:
# The sum of first 100 numbers is5050
# The sum of odd numbers2500  
# The sum of even numbers 2550
