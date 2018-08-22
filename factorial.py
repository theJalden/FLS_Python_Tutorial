# Number -> Number
# Returns n! = n * (n-1) * ...  * 2 * 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Number -> Number
# Returns n! = n * (n-1) * ...  * 2 * 1
def factorialLoop(n):
    acc = 1
    while n > 1:
        acc *= n
        n -= 1

    return acc

import time

start1 = time.time()
v1 = factorial(500)
print(time.time() - start1)


start2 = time.time()
v2 = factorial(500)
print(time.time() - start2)
