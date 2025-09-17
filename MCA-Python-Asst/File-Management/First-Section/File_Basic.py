
'''
1. Write a python program to:
    a. Open a text file in write mode and write some data into it.
    b. Read and print the contents using read() method.
    c. Close the file properly and print a message once closed.
'''


print("=="*10)
with open(r'C:\Users\user\Desktop\Manish\ASST-7\info.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()
print("=="*20)
print("File Closed. Visit Again.")    