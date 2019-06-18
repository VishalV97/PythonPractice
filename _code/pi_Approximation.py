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

