age = int(input("What is your age(Please enter in numbers): "))

if age >= 150:
    print("Liar")
elif age >=80 and age < 150:
    print("Tell me your secret!")
elif age >=55 and age < 80:
    print("Ok Boomer")
elif age >= 40 and age < 55:
    print("Hello Gen X")
elif age > 24 and age < 39:
    print("Hey Millenial")
elif age <= 24:
    print("Hola Gen Z")
else:
    print("LOL! Tell me your secret")
    
#+++++++++++++++++++++++++++++++++++++++++++++++++

print("Let's test your memory")
print("How many people do you think you follow online?")
following = int(input())
subs = []

def number(following):
    if following <= 10:
        print('Thats awesome! Minimalist style. List it down plz')
    elif following > 10 and following < 30:
        print('Thats manageable. Care to list them down?')
    elif following >= 30 and following < 60:
        print('How do you really keep track of all of them?. Well i don\'t believe you. List them down plz')
    elif following >= 60:
        print('That\'s a lot! Can you name them all?')
    num = 0
    while num < following:
        total = input("Type the name and press enter.(Leave empty and enter to finish): ")
        subs.append(total)
        print(subs)
        num += 1
        if total == '':
            break

number(following)

if len(subs) < following:
    print("Thats understandable. You can't name every one of them.")
       
elif len(subs) == following:
    print("Thanks a lot for taking your time to input every one of them.\n Its time to eliminate one. Which one would it be")
    print("Type the name to remove them")
    choice = input('Enter the name: ')
    if choice != '':
        subs.remove(choice)
        print(subs)