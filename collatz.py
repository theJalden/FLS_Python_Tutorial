# Number -> list of Numbers
# Take a number, return the list of numbers going down to 1
# ex 3 -> [3 10 5 16 8 4 2 1]
def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n//2)
    else:
        return [n] + collatz(3*n +1)
