a = 0
b = 1
num = []
even = []
while b < 4000000:
    c = a + b
    if c >= 4000000:
        break
    num.append(c)
    a = b
    b = c
print(num)
for x in num:
    if x % 2 == 0:
        even.append(x)
print(sum(even))