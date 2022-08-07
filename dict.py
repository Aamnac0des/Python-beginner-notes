#allows us to work with key-value pairs...also known as hash maps or associative arrays.....2 linked values where the key is the UNIQUE IDENTIFIER where we can find our data and the VALUE is that DATA.

student = {'name': 'aamna', 'age': '20', 'courses': ['math', 'bio']} 
print(student)

print(student['name'])
print(student['courses'])   #accessing values through their key

student_2 = {1: 'aamna', 'age': '20', 'courses': ['math', 'bio']}
print(student_2[1])  #key can be of int type

#GET method: returns none if the key doesnt exists
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'not found'))  #you may set the desired default value in case the key doesnt exist BY ADDING A SECOND ARGUMENT.

#adding new entry to our dict
student['phone'] = '555-5555'
print(student)

student['name'] = 'iqra'
print(student)  #if a value already exists, it'll get updated

#to update multiple values at once..update method..takes dict as an argument
student.update({'name': 'sehrish', 'age': 21, 'phone': '444-4444'}) 
print(student)

#DELETING specific key and its value

#DEL method
del student['age']
print(student)

#POP method...returns the removed value 
phone = student.pop('phone')  #phone variable would contain the value that we popped off
print(student)
print(phone)

#LOOPING through all the keys and values of our dict

# to find how many kleys we have in our dict
print(len(student))

print(student.keys())  #gives all of the keys
print(student.values())  #gives all of the values
print(student.items())  #returns pairs of key-value pairs

for key, value in student.items():
    print(key, value)







