import random

def approxPi(n):
    sum = 0
    for i in range(0,n):
        if i % 2 == 0:
            sum += ((1)**i)/(2*i + 1)
        else:
            sum += (-1**i)/(2*i + 1)
    Pi = 4*sum
    print("Here is pi's approximation to %dth accuracy: " % n + str(Pi))

while True:
    val = random.randint(1,100000)
    if val % 37 == 0:
        print("%d is divisble by 37 " % val)
        break
    else:
        print(approxPi(val))


'''
Approximates the value of pi to an nth degree using the mathematical series formula for the calculation of pi.

n represents the upper limit of the series in which the series is calculated. 

Second part of code generates a random number between 1 and 100000 and determines if the number is divisible by
37, if not it runs the code above to that number's accuracy. 
'''

