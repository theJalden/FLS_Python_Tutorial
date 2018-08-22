# Fibonacci : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

import time


for ii in range(1,40):
    start_time1 = time.time()
    result1 = fibo(ii)
    print(ii, result1, time.time() - start_time1)



