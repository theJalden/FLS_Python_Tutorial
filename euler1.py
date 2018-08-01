
# Number -> Boolean
# Return True if given number is a multiple of 3
# False otherwise
def isMultipleOf3(n):
    return (n % 3) == 0

# Number -> Boolean
# Return True if given number is a multiple of 5
# False otherwise
def isMultipleOf5(n):
    return (n % 5) == 0


summa = 0
for x in range(1000):
    if isMultipleOf3(x) or isMultipleOf5(x):
        summa += x

print(summa)
