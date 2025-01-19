dog=dict()
dog={"name":"chunmun","color":"white","weight":"15kg","breed":"pomeranian"}
print(dog)
student={ "first_name":"Rudra", "last_name":"Chowdhary", "gender": "Male", "age": 24, "marital status":"Unmarried", "skills":["React","NodeJs"], "country": "IN", "city": "GZB","address": "XYX"}
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('HTML')

print(student.items())  #Converted dict to a tuple of key value pairs

student.pop('age')
print(student)

del(dog)    #goodbye chunmun