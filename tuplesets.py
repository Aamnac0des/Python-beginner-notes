#you can't modify a tuple..it's immutable unlike lists

#list1 = ['history', 'math', 'chem', 'bio']
#list2 = list1
#print(list1)
#print(list2)

#list1[0] = 'art'   #changed the value at zeroth index
#print(list1)
#print(list2)  #both lists changed because they're the same mutable objects

#immutable
#tuple1 = ('history', 'math', 'chem', 'bio')
#tuple2 = tuple1
#print(tuple1)
#print(tuple2)

#tuple1[0] = 'art'
#print(tuple1)
#print(tuple2)   #error since its immutable, hence we cant append, delete etc, rest it behaves the same..you can loop through them and access values.



#SETS
#Values that are unordered and have no duplicates
courses = {'bio', 'math', 'chem'}
print(courses)  #not in order..prints in random orders with every execution
#courses = {'bio', 'math', 'chem', 'math'}
print(courses)  #doesnt print duplicates

#membership test: to test if a value is part of the test..sets do this a lot more effeciently
print('bio' in courses)  #returns true/false

courses2 = {'bio', 'math', 'phy'}
print(courses.intersection(courses2))  #returns common values
print(courses.difference(courses2))   #returns courses not incommon
print(courses.union(courses2))  #combines both sets

CREATING EMPTY LISTS, TUPLES AND SETS
emp_list = [] 
#or
emp_list = list()

emp_tuple = ()
#or
emp_tuple = tuple()

emp_set = {}  #WRONG..creates empty dictionary
emp_set = set()


