def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

#Closure is used to access variables outside the function. In this case, the variable ten is accessed outside the function add. The function add is returned and assigned to closure_result. The closure_result is called with an argument 5 and 10. The function add adds the argument to the variable ten. The result is 15 and 20 respectively.