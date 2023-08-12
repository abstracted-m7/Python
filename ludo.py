
import random
while True:
    print("1. Roll the dice. ")
    print("2. Exit from this game.")
    user=int(input("What you want to do \n : "))
    if user==1:
         number=random.randint(1,6)
         print(number)
    else:
        break