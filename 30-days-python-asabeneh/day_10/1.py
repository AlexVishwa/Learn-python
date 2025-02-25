for a in range(10):
    print(a)
a=0
while(a < 10):
    print(a)
    a=a+1
for a in range(10,0):
    print(a)
a=10
while(a>0):
    print(a)
    a=a-1
# Output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

for i in range(1,8):
    pattern=['#']
    for j in range(1,i):
        pattern.append('#')
    print(f'{pattern}')

#Output:
# ['#']
# ['#', '#']
# ['#', '#', '#']
# ['#', '#', '#', '#']
# ['#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
for i in range(1,8):
    # pattern=tuple()
    for j in range(1,8):
        # pattern.extends(['#'])
        pass
    # print(f'{pattern}')
    pass
#AttributeError: 'tuple' object has no attribute 'extends'
# Needed Output:
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
# ['#', '#', '#', '#', '#', '#', '#']
for i in range(1,11):
    j=i*i
    print(f'{i}\tx\t{i}\t={j}')
# 1       x       1       =1
# 2       x       2       =4
# 3       x       3       =9
# 4       x       4       =16
# 5       x       5       =25
# 6       x       6       =36
# 7       x       7       =49
# 8       x       8       =64
# 9       x       9       =81
# 10      x       10      =100
list1=['Python','Django','Sql','Xuz']
for o in list1:
    print(o)

print('Even numbers')
for i in range(100):
    if(i%2==0):
        print(i)

print('odd numbers')
for i in range(100):
    if(i%2!=0):
        print(i)