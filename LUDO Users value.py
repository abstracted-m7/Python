
# LUDO Game

# Condition:-  Input 2 user's value... Which user's score is 57,the user is winner.

import random
a=0
b=0
x=0
y=0
c=0
d=0
while True:
    print("1.roll dice  2.Exit")
    user1=int(input("User1. What you want to do(1 or 2): "))
    if user1==1:
        number = random.randint(1,6)
        print(number)
        x=x+number
        

        if number==6:
            user1=int(input("User1. what you want to do?: "))
            if user1==1:
                number = random.randint(1,6)
                print(number)
                a=a+number

                if number==6:
                    user1=int(input("User1. what you want to do?: "))
                    if user1==1:
                        number = random.randint(1,6)
                        print(number)
                        b=b+number
                    else:
                        pass
            else:
                pass


        else:
            pass

        
        
    else:
        quit()

    user2=int(input("User2. What you want to do(1 or 2): "))
    if user2==1:
        number = random.randint(1,6)
        print(number)
        y=y+number

        if number==6:
            user2=int(input("User2. what you want to do?: "))
            if user2==1:
                number = random.randint(1,6)
                print(number)
                c=c+number

                if number==6:
                    user2=int(input("User2. what you want to do?: "))
                    if user2==1:
                        number = random.randint(1,6)
                        print(number)
                        d=d+number
                    else:
                        pass
            else:
                pass


        else:
            pass

        
        
    else:
        quit()

        

    print( )

    x=(x+a+b)
    y=(y+c+d)



    print("user1 score",x)
    print("user2 score",y)

    if x>=57:   
        print("User1 win the match.")
        quit()
    elif y>=57:
        print("Use2 win the match.")
        quit()
    else:
        pass