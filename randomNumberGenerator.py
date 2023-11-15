import random
import math

min = int(input('min range: '))
max = int(input('max range: '))

x = random.randint(min, max)
#keep count
count = 0

while count < math.log(max - min + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(max - min + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")