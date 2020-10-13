n = 1
num = []
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        num.append(n)
    n += 1
print(sum(num))