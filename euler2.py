
f1 = 1
f2 = 2
total = 0

while f2 < 4000000:
    if f2%2 == 0:
        total += f2
    t2 = f2 + f1
    t1 = f2
    f2 = t2
    f1 = t1
print(total)    
