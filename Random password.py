
#random password

import random
password = int(input("Enter the length of password : "))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p= "".join(random.sample(s,password))
print(p)