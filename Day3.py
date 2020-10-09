#Create a list using [] square brackets
#L for List looks like a [L] square bracket
#List is ordered.
#List is changeable
#List allows duplicate values

list = ['a', 'b', 3]

print(list)

#Access the list
print(list[0])

#Negative indexes also applies
print(list[-1])

#Change the value in a list
list[2] = 'c'
print(list)

#Find the length of a list
print(len(list))

#To add the item to a list at the end, use append()
list.append('d')
print(list)

#To add the item at a specific place, use insert()
list.insert(2, 'c')
print(list)

#Remove the item from a list using remove()
list.remove('d')
print(list)

#You can also remove using pop()
#If you pop() without an index, the last item is removed
#If you specify the index, that particular item is removed

list.pop()
print(list)
list.pop(0)
print(list)

#pop() and remove() are little confusing isn't it?
#pop() should have index
#remove() should have value
#More practice is needed.

#You can also use the del keyword
del list[1]

print(list)

#del keyword is also used to delete the list completely
del list

print(list) #Returns the class type, which is a list

#To empty the list, use clear()
#Create a new list

new = [1, 2, 3]
print(new)

new.clear()
print(new)

#To copy the contents of a list, use copy()
copy1 = ['docx', 'xls', 'pptx']

copy2 = copy1.copy()

print(copy1)
print(copy2)

#Now i am adding a content to copy 1, see what happens.

copy1.append('mp4')

print(copy1)
print(copy2) #This list dont get the new value. Wonder why?

#How about we do this?

list1 = ['apple', 'banana']
list2 = list1

print(list1)
print(list2)

list1.append('cherry')

print(list1)
print(list2)

#Got it?
#It also works the other way around.

list2.append('dragonfruit')
print(list1)
print(list2)

#There is another way to copy the list.
#Using built in list()

a = [1, 2, 3]
b = list(a)

print(a)
print(b)

a.append(4)

print(a)
print(b)

#We can simply join two lists using concatenation that is +

x = [1, 2]
y = [3, 4]

print(x)
print(y)

z = x + y
print(z)

#Yep. There is another way to add lists. Using extend()

apps = ['fb', 'ig']
brow = ['ch', 'fi']

print(apps)
print(brow)

apps.extend(brow)

print(apps)
print(brow)

#But it is not like using + operator. It extends the contents permanently

#Last but not the least, it is possible to create a list using list()

abc = list((1, 2, 3, 4, 4, 6)) #Dont forget the double (()) round brackets
print(abc)
print(type(abc))

