lang = 'python'

if lang == 'python':
    print('is true')

#difference btw '=' and '==' : '=' used for assigning values and '==' tests for equality 

#COMPARISONS:
# equal: tests for equality  ==
# not equal:                 !=
# greater than:              >
# less than:                 <
# greater or equal:          >=
# less or equal:             <=
# object identity:           is......using 'if', we're actually checking if the values have the same id whether they're the same object in memory

if lang == 'python':
    print('lamg is python')
else:
    print('no match')    #if our IF satement evaluates to true, it''ll print code within that block and will never execute the else block, isnce it already met the condition.

lang = 'java'
if lang == 'python':
    print('lamg is python')
else:
    print('no match')    #if it doesnt, it''ll drop down to our else statement and will execute that code

#to check for multiple lang and execute diff codes for each one that we encounter...elif
lang = 'java'
if lang == 'python':
    print('lamg is python')
elif lang == 'java':
    print('lang is java')
else:
    print('no match')    #if none of the conditions are met, ELSE statement will be executed.

#SWITCH CASE STATEMENT: it's a way to check multiple values. Python doesn't have a switch case because the IF, ELIF and ELSE statements are clean enough to do this.

#SOME BOOLEAN OPERATIONS: and, or & not

user = 'admin'
logged_in = True

#execute some code only if the 'user' is 'admin' and 'logged in' is 'true'...AND
if user == 'admin' and 'logged_in':
    print('admin pageee')
else:
    print('bad credentials')

#if one of them evaluates to true....OR
user = 'admin'
logged_in = False
if user == 'admin' or logged_in:
    print('admin pageee')
else:
    print('bad credentials')    #only one needed to be true

#NOT operation is used to switch a boolean...will change a TRUE to a FALSE and vice versa
user = 'admin'
logged_in = False
if not logged_in:        #NOT logged_in will evaluate to TRUE, since our logged_in = FALSE...NOT FALSE means true
    print('please log in')
else:
    print('welcome')

#difference between IS and ==
#object identity(is) test if 2 objects have the same id which means if they are the same object in memory. 2 objects can be equal and not be the same object in memory...for exaple
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  #evaluates to true as a and b are equal
print(a is b)  #evaluates to false because they';re 2 different objects in memory..these locations can be printed usinmg built-in id function
print(id(a))
print(id(b))   #ids are different

#if instead we write something like..
c = [2, 3, 4]
d = c
print(c is d)   #evalautes to true because now they're the same object in memory....id of c is equal to id of d

#FALSE VALUES:...what all values evaluates to fase in python
    #false
    #none
    #zero of any numeric type
    #any empty sequence. for eg, '', (), []
    #any empty mapping. for eg, {}
#almost everything else evaluates to rue

















