#Day13

#Work with Json data using json package.
#Don't know what that means.
#Anyways.... w3schools guide, so

import json

#Convert from JSON to python using json.loads()

a = '{"c": "abc", "b": 123}'

'''Even though a is a dictionary with key:value pairs,
notice the quotes '' around them

Also, for some reason, 'single quotes need to be outside the paranthesis'
and "double quotes need to be included for strings inside the paranthesis"
'''

b = json.loads(a)

print(a)
print(b)

print(type(a))
print(type(b)) #See how we converted string to a dictionaray

'''
You can convert any of the following to a JSON string using json.dumps()

int
float
string

True
False
None

tuple
list
dictionary
'''

int = 42
int_c = json.dumps(int)
print(int_c)
print(type(int_c)) #See, we've converted int to json str

float = 2.3
float_c = json.dumps(float)
print(float_c)
print(type(float_c)) #See we've converted float to json str

str = "string"
str_c = json.dumps(str)
print(str)
print(type(str))
print(str_c)
print(type(str_c)) #What's the purpose of converting a str to json str?

true = True
true_c = json.dumps(true)
print(true_c)
print(type(true_c))

false = False
false_c = json.dumps(false)
print(false_c)
print(type(false_c))

none = None
none_c = json.dumps(none)
print(none_c)   #Returns null
print(type(none_c))

tuple = (1, 2, 3)
tuple_c = json.dumps(tuple)
print(tuple_c)
print(type(tuple_c))

list = [1, 2, 3, 4]
list_c = json.dumps(list)
print(list_c)
print(type(list_c))

dict = {'a': 10, 'c': 8, 'b': 7}
dict_c = json.dumps(dict, indent=4) #See anything different from prev json.dumps()?
#indent parameter gives exactly what the name says, indentation
print(dict_c)
print(type(dict_c))

dict_d = json.dumps(dict, indent=4, separators=(" & ", " = ")) 
#separators = used to separate key value pairs with custom symbols
print(dict_d)

dict_sort = json.dumps(dict, indent=4, sort_keys=True)
#sort_keys = Used to sort the keys
#Remember, it has to be True / False
#It will only sort the keys. Not the values
print(dict_sort)