#Sets use curly brackets {}

set = {1, 2, 2, 3}

print(set)

#Sets won't allow duplicate values
#Sets are unordered and so unidexed
#Sets cannot be changed

#New value can be added using add()

set.add("a")

#Multiple new values can be added using update()

set.update([3, 5, 7]) #Notice those square brackets.

print(set)

print(len(set))

#Set can be set using set()
#Remember to use (())

abc = set(('new', 'set'))
print(abc)

#To remove specific values, use remove()

set.remove('a') #If the value is not found, python gives an error
print(set)

#To remove specific values, you can also use discard()

set.discard(7) #If the value is not found, python wont give an error
print(set)

#To remove items from the set, use pop()
#We dont know which values python will remove from the set,
#Since it is unordered

set.pop()
print(set)

#To clear the contents from the set, use clear()

abc.clear()
print(abc)

#To delete the set permanently, use del

del abc

#We can join two sets using union()
#Yeah sets have union() unlike amazon warehouse employees

a1 = {1, 2, 3}
a2 = {'a', 'b', 'd'}

a3 = a1.union(a2)
print(a3)
print(a1)
print(a2)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Dictionary

#Dictionary can be created using {} curly brackets
#But what is the difference between a set and a dictionary then?

#Dictionary has name: value pairs

dict = {
"a":"abc",
"b": 1 }
print(dict)

#Dictionary is unordered
#Dictionary is changeable
#Dictionary is indexed

#Access item of the dict
print(dict['b'])

#You can get the same output using get()
print(dict.get('b'))

#Change the value of a dictionary
dict['b'] = "def"
print(dict)

#Get the length of the dictionary
print(len(dict))

#Add the new key value pair just by using a new index
dict['c'] = "ghi"
print(dict)

#To remove the items, use pop() but use the key name
#Arguments in pop is mandatory with dictionaries
dict.pop('c')
print(dict)



#The last added item can be removed using popitem()
dict['z'] = "zzz"
print(dict)
dict.popitem()
print(dict)

#A dictionary can have another dictionary

person1 = { "name": "Roger",
"age": 43,
"sex": "m",
"children" :
    {
    "daughter1": "emily",
    "son1" : "abraham",
    "son2" : "john"
    }
}
print(person1)

#A dictionary can be copied using copy()

person2 = person1.copy()
print(type(person2))

#clear() clears the dictionary
person2.clear()
print(person2)

#del deletes the dictionary.
#You know how to delete the individual key:pair ----> del dict['key']
del person2

#Dictionary can also be created using dict()
#Unlike lists, tuples and sets, dictionaries dont need (())
#() is enough. But, Yes, But, there's always a but
#But, assigning requires =


new = dict(a="abc", b=123, c='def', d = "456")

print(new)