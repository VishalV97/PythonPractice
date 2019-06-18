import time as time

lo = 0
high = 100
attempts = 0
print("Please think of a number between 0 and 100!")
time.sleep(5)
while True:
    guess = (lo + high)//2
    print("Is your secret number", str(guess) + "?")
    sel = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if sel == 'h':
        high = guess
        attempts += 1
    elif sel == 'l':
        lo = guess
        attempts += 1
    elif sel == 'c':
        print("Game over! Your secret number is " + str(guess))
        print("Number guessed in %d iterations!" % (attempts+1))
        break
    else:
        print("Sorry, I did not understand your input")