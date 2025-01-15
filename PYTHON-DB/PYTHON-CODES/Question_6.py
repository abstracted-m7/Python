
#Question 6: Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).

# Import module to generate random numbers
import random

# Create a function
def roll_dice():
    return random.randint(1, 6) #random integer genarate between 1 and 6

# call the function and store the number in a variable
dice_roll = roll_dice()
print(f"Dice roll result: {dice_roll}")
