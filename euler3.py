
# Number -> Boolean
# Returns true if the given number is prime, false otherwise
def isPrime(num):
    for xx in range(2, num//2 + 1):
        if num % xx == 0:
            return False
    return True

# Number -> Number
# Returns the next prime number greater than the given number
def nextprime(num):
    n = 1
    while not isPrime(num + n):
        n += 1

    return num+n

n = 600851475143
test_prime = 2
highest_prime = 0
largest_prime = n

while test_prime < largest_prime:
    if n%test_prime == 0:
         highest_prime == test_prime
    
    

          

