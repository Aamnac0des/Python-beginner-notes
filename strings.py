message = "Hello world"
print(message.lower())   
print(message.upper())
print(message.count("Hello"))  #no of occurances
print(message.count("l"))      #no of l
print(message.find("world"))   #returns index of the word/ if the word doesnt exists it'll return -1
print(message.replace("world", "universe"))  #rreplaces word in the string

greeting = "hello"
name = "aamna"
message = greeting + ', ' + name + '. Welcome'
print(message)

#or

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#or

message = f'{greeting}, {name}. Welcome!'  #f string
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'  #f string
print(message)

print(dir(name))  #shows all the attributes and methods that we have access to with that variable

print(help(str))  #runs on the class/gives us a lot more info..tells what's available..what methods do, hat arguments they take

print(str.lower)
