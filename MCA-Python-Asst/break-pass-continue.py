# Demonstrate the use of break, continue, and pass in separate programs:
#    • Exit a loop early using break.
#    • Skip printing a specific number using continue.
#    • Use pass in a loop body placeholder.

num = 10
for i in range (num):
    if i == 2:
        continue
    if i == 3:
        pass
    if i == 5:
        break
    print(i)



for i in range(5):
    pass  

print("For loop completed.")
