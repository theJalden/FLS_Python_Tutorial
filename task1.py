
for xx in range(1,100):
    if xx%3 == 0 and xx%5!=0:
        print("Fizz")
    elif xx%5 == 0 and xx%3!=0:
        print("Buzz")
    elif xx%3 ==0 and xx%5 ==0:
        print("FizzBuzz")
    else:
        print(xx)
         
