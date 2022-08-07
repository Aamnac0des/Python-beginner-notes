courses = ['history', 'math', 'physics', 'compsci']
print(courses)
print(len(courses)) #no of list items
print(courses[0])   #accessing each element through its index
print(courses[3])   #range of index = len-1
print(courses[-1])  #-1 gives element at the last index

#slicing
print(courses[0:2]) #first index is inclusive, second is not
print(courses[:2])  #starts from beginning
print(courses[2:])  #from second index till the end

#some methods to modify our list

courses.append('art')
print(courses)  #adds element to the end of the list

courses.insert(0, 'bio')  #insert takes two arguments...first - location, second - value itself
print(courses)
courses_2 = ['chem', 'phy']
#courses.insert(0, courses_2)
#print(courses)  #inserts whole list at one index as a singke element
#print(courses[0])

courses_2 = ['chem', 'phy'] 
courses.extend(courses_2)
print(courses)  #extend is used to add multiple values to our list

#removing elements
courses.remove('chem') #will delete chem
print(courses)
popped = courses.pop()  #removes last value from the list......pop also returns the value popped
print(courses)
print(popped)

#sorting list
courses.reverse()  #reverses the list
print(courses)

courses.sort()  #sorts the list in alphabetical order
print(courses)
alist = [1, 2, 8, 4, 3]
alist.sort()  #sorts the list in asc order
print(alist)

alist.sort(reverse = True)  #sorts in desc order
courses.sort(reverse = True)
print(alist)
print(courses)

#sorting the course list without altering the orignal list...using SORTED function
sorted_courses = sorted(courses)
print(sorted_courses)

#SOME OTHER BUILT INS

print(min(alist))  #returns min  value
print(max(alist))
print(sum(alist))

#finding values wihtin a list

print(courses.index('compsci'))  #index of compsci

print('chem' in courses)  # checks if the value is in list

#may also loop through items
for item in courses:
    print(item)


#to access the index + value can be done through enumerate function...returns the index we're on and the value
for index, course in enumerate(courses):
    print(index, course)


for index, course in enumerate(courses, start=1):
    print(index, course)
       

#trurning our lists into STRINGS

course_str = ', '.join(courses)  #string seperated by ,
print(course_str)

new_list = course_str.split(',')
print(new_list)





