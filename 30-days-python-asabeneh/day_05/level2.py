ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def bsort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if(arr[i]>arr[i+1]):
                temp=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
    return arr

print(bsort(ages))
# Output:
# [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

min=ages[0]
max=ages[-1]
print(f"The minimum age is {min}")
print(f'The maximum age is {max}')
# Output:
# The minimum age is 19
# The maximum age is 26
ages.append(min)
ages.append(max)
print(ages)
# Output:
# [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
bsort(ages)
if((len(ages)-1)%2==0):
    median=ages[int((len(ages)-1)/2)]
else:
    median=int((ages[int((len(ages)-1)/2)]+ages[int((len(ages)-1)/2)+1])/2)
print(median)
# Output
# 24
sum=0
for i in range(len(ages)-1):
    sum=sum+ages[i]
avg= int(sum/(len(ages)-1))

print(f'the average age is {avg}')
# # Output:
# the average age is 22
ran=ages[-1]-ages[0]
print(f'The range of age is {ran}')
# The range of age is 7
a=abs(min-avg)
b=abs(avg-max)
if(a>b):
    print("Minimum is much lesser than Average")
else:
    print("Maximum is larger than Average")
    # Output:
    # Maximum is larger than Average

# Questions
    # Find the middle country(ies) in the countries list
    # Divide the countries list into two equal lists if it is even if not one more country for the first half.
    # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
