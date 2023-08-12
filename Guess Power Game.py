


#Test your guessing power

#Condition:- If your guessing number is correct then all right.And if your guessung number is wrong then you will get three chances..

import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the number:  "))
    if user==number:
        print("Hurray!!")
        print(f"Your guessing number is correct.The number is {number}")
        break
if user !=number:
    print(f"Your guessing number is incorect. The correct number is {number}")




