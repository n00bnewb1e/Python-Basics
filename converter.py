#Converter
weight = 2.20462 #Don't ask me where this number comes from. Math, you know :D

def kg_to_lbs(kg):
    lbs = kg * weight
    print(lbs)
    
def lbs_to_kg(lbs):
    kg = lbs / weight
    print(kg)
    
height = 30.48 #Again, math, you know

def cm_to_ft(cm):
    ft = cm / height
    print(ft)
    
def ft_to_cm(ft):
    cm = ft * height
    print(cm)
    
height2 = 2.54 #For inches conversion

def cm_to_inch(cm):
    inch = cm / height2
    print(inch)
    
def inch_to_cm(inch):
    cm = inch * height2
    print(cm)
    
def mile(mile):
    #You can find these numbers with a simple google search
    yards = 1760 * mile 
    feet = 5280 * mile
    metre = 1609 * mile
    km = 1.609 * mile
    print(mile, " mile is equal to ", yards, " yards")
    print(mile, " mile is equal to ", feet, " feet")
    print(mile, " mile is equal to ", metre, " metres")
    print(mile, " mile is equal to ", km, " kms")