#Q1. write a python program to accept two numbers from the user and calculate ADDITION.
a=float(input("Enter the first number = "))
b=float(input("Enter the second number = "))
c=a+b
print("Total number is =",c)


#Q2. Write a python program to accept sides from the user and find the area of a SQUARE,RECTANGLE.
#i)SQUARE
a=float(input("Enter the side value = "))
c=a**2
print("The square value is = ",c)
#ii)RECTANGLE
a=float(input("Enter the length = "))
b=float(input("Enter the wigth = "))
c=a*b
print(" The Ractangle value is = ",c)


#Q3. Write a pythin program to accept radius from the user and calculate the area and cricumaferances of the circle.
#i)AREA
r=float(input("Enter the radius value = "))
a=(22/7)*(r**2)
print("The circle's Area is = ",round(a))
#ii)CRICUMAFERANCES
r=float(input("Enter the radius value = "))
c=2*(22/7)*r
print("The circle's Cricumaferances is = ",round(c))

#Q4. Write a python program to accept two numbers from the user and SWAP between two numbers using a third variable.
a=float(input("Enter the first number = "))
b=float(input("Enter the second number = "))
temp=a
a=b
b=temp
print("The SWAP number is= ",a,b)

#Q5. Write a python program to accept two numbers from the user and SWAP between two numbers without using a third variable.
a=float(input("Enter the first number = "))
b=float(input("Enter the second number = "))
a=a+b
b=a-b
a=a-b
print("The SWAP number is = ",a,b)


#Q6. Write a python program to accepts days from the user and calculate the DAYS,MONTH,YEARS from the total numbers of days.
d=int(input("Enter number of days: "))
y=d//365
m=(d-y*365)//30
day=(d-y*365-m*30)
print("Total year= ",y)
print("Total months= ",m)
print("Total days= ",day)

#Q7. Write a python program where x=(a+b)**2/(a-b)**2
a=float(input("Enter the value of a = "))
b=float(input("Enter the value of b = "))
x=(a+b)**2
y=(a-b)**2
c=x/y
print("Total is = ",c)

#Q8. Write a python program where 2*(a+b)*(a-b)
a=float(input("Enter the value of a= "))
b=float(input("Enter the value of b= "))
x=2*(a+b)*(a-b)
print("Total is = ",x)

#Q9. Write a python program that will take input temperature as celsius and print Faharanhit and Kelvin.
c=float(input("Value of celsius = "))
k=(c+273.15)
print("The Kelvin value is = ",k)
f=(9/5)*c+32
print("The Faharanhit value is = ",f)


#Q10. Write a python program that will be take Basic Salary of an employee and print cash in hand.
#{HINT: DA=20% Of Basic, TA=5% of Basic, HRA=10% of Basic, Salary= BASIC+DA+TA+HRA
#SALARY.PY
a=float(input("Enter the Basic Salary = "))
DA=a*(20/100)
print("Total amount of DA =",DA)
TA=a*(5/100)
print("Total amount of TA= ",TA)
HRA=a*(10/100)
print("Total amount of HRA= ",HRA)
print(a+DA+TA+HRA)


#Q11. Write a python program to check whether a given number is positive or not.
a= float(input("Enter the number = "))
if a>0:
    print(" This Number is positive.")
elif a<0:
    print("This number is negative.")
else:
    print("No Number")
    

#Q12. Write a python program to check if a number is even or odd.
a=int(input("Enter the number = "))
if a%2==0:
    print("This number is even.")
else:
    print("This number is odd.")



#Q13. Write a python program to find the greater among two numbers.
a=int(input("Enter the first number= "))
b=int(input("Enter the second number = "))
if a>b:
    print("The first number is Greater.")
else:
    print("The second number is Greater.")


#Q14. Write a python program to check whether a parson is an adult or Tenager.
a=int(input("Enter the parson's Age = "))
if 18<a:
    print("You are an Adult.")
else:
    print("You are an Tenager.")

#Q15. Write a python program to check whether a number is divisible by 2 and 3.
a=float(input("Enter the number = "))
if (a%2==0) and (a%3==0):
    print("This number is divisible.")
else:
    print("This number is not divisible.")

#Q16. Write a python program to check whether a number is divisible by 3 and 5
a=int(input("Enter the number = "))
if (a%3==0) and (a%5==0):
    print("This number is divisible.")
else:
    print("This number is not divisible.")
    

#Q17. Write a python program to check the greatest among three number.
a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
c=int(input("Enter the third number= "))
if (a>b) and (a>c):
    print("The first number is greatest.")
elif (b>a) and (b>c):
    print("The second number is greatest.")
else:
    print("The third number is greatest.")

#Q18. Write a python program to check the greatest among 3 number using the ternary operator.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if(b<a>c):
    print("The first number is greatest.")
elif (a<b>c):
    print("The second number is greatest.")
else:
    print("The third number is greatest.")

#Q19. Write a python program to check the greatest among 3 number using the ternary operator.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
max=a if (a>b) else b
max1=c if (c>max) else max
print("This is a greatest number : ",max1)

#Q20. Write a python program to check if a year is a leap or not.
a=int(input("Enter the year = "))
if (a%4==0):
    print(a,"Its leap year.")
else:
    print(a,"Its not a leap year.")

#Q21. Write a python programto calculate the electric bill amount, acording to the given chart.
#{Hints: [1-100 unit= 5/-],[101-200 unit= 7/-],[201-300 unit= 10/-],[above 300= 15/-]}
a=int(input("Enter the total unit = "))
if (a>=1) and (a<=100):
      print("Amount par unit = 5/-")
      print("Total bill =",a*5)
elif (a>=101) and (a<=200):
    print("Amount par unit = 7/-")
    print("Total bill = ",a*7)
elif (a>201) and (a<300):
    print("Amount par unit = 10/-")
    print("Total bill = ",a*10)
else:
    print("Amount par unit = 15/-")
    print("Total bill = ",a*15)


#Q22.Write a python program to calculate the student grade using if-else.
#[Hints: if percentage>85 print A grade/if percentage>85 & parcentage<75 print B Grade/ if percentage<75 & percentage>=50 print C grade/if percentage<30 & percentage>=50 print D grade/ if percentage<30 print fail.
m=int(input("Marks Percentage = "))
if m>85:
    print("A Grade")
elif m<85 and m>=75:
    print("B Grade")
elif m<75 and m>=50:
    print("C Grade")
elif m<50 and m>=30:
    print("D Grade")
else:
    print("This Student Is Faill.")


#Q23. Write a python program to check whether the last digit of a number is divisible by 3 or not.
a=int(input("Enter the number = "))
if(a%10%3==0):
    print(a,"Its divisible by 3")
else:
    print(a,"Its not divisible by 3")


#Q24.Write a python program to check whether a number is buzz or not.
a=int(input("Enter the number = "))
if a%10==7:
    print("Its a buzz number.")
elif a%7==0:
    print("Its a divisible buzz number.")
else:
    print("Its not a buzz number.")
    

#Q25. Write a python program to check whether a number is automorphic or not.
a=int(input("Enter the number = "))
b=a**2
if b%a==0:
    print("This number is automorphic.")
else:
    print("This number is not automorphic.")


#Q26. Write a python program to input any alphabet and check whether it is vowel or consonant.
ch=input("Enter the charecter = ")
if (ch=='A' or ch== 'a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print("Its a Vowle.")
else:
    print("Its a Consonant.")

#Q27. Write a python program to input any character and check whether it is alphabet,digit or Special Character.

import string as s
var=input("Enter the Input = ")
if var in s.ascii_letters:
    print("This is an alphabet.")
elif var in s.digits:
    print("This is a digit.")
elif var in s.punctuation:
    print("This is a Spacial_Character.")


#Q28. Write a python program to check whether a character is uppercase or lowercase alphabet.

import string as s 
ch = input("Enter the value : ")
if ch in s.ascii_uppercase:
    print("This value's style in UPPERCASE." )
elif ch in s.ascii_lowercase:
    print("This value's style in LOWERCASE.")


#Q29. Write a python program to calculate profit or loss.

a=float(input("Enter the cost of product : "))
b=float(input("Enter the sale price of product : "))
if (b>a):
    c=b-a
    print("Your profit is :",c,"/-")
elif(b<a):
    d=a-b
    print("Your loss is : ",d,"/-")
print("Thank you")

#Q30. Write a python program to input marks of five subjects PHYSICS , CHEMISTRY , BIOLOGY , MATHEMATICS and COMPUTER calculate percentage and grade according to following.
#percentage > = 90%:Grade A
#percentage > = 80% Grade B
#percentage > = 70% Grade C
#percentage > = 60% Grade D
#percentage > = 40% Grade E
#percentage  <  40% Grade F

phy=int(input("Enter the number of PHYSICS : "))
chem=int(input("Enter the number of CHEMISTRY : "))
bio=int(input("Enter the number of BIOLOGY : "))
math=int(input("Enter the number of MATHEMATICS : "))
clp=int(input("Enter the number of COMPUTER : "))
a=(phy+chem+bio+math+clp)
b=a/5
print("Your total parcentage : ",b,"%")
if b>90:
    print("Your GRADE = A")
elif b<=89 and b>=80:
    print("Your GRADE = B")
elif b<=79 and b>=70:
    print("Your GRADE = C")
elif b<=69 and b>=60:
    print("Your GRADE = D")
elif b<=59 and b>=40:
    print("Your GRADE = E")
else:
    print("Your GRADE = F")


#Q31. Write a python program to input basic salary of an employee and calculate its Gross salary according to following.
#BASIC SALARY < = 10000:HRA=20%,DA=80%
#BASIC SALARY < = 20000:HRA=25%,DA=90%
#BASIC SALARY > 20000:HRA=30%,DA=95%

basicsalary=float(input("Enter the BASIC PEY = "))
if(basicsalary<=10000):
    HRA=basicsalary*(20/100)
    print("Your HRA = ",HRA)
    DA=basicsalary*(80/100)
    print("Your DA = ",DA)
    a=basicsalary+HRA+DA
    print("Your total SALARY = ",a)
elif(basicsalary<=20000):
    HRA=basicsalary*(25/100)
    print("Your HRA = ",HRA)
    DA=basicsalary*(90/100)
    print("Your DA = ",DA)
    b=basicsalary+HRA+DA
    print("Your total SALARY = ",b)
elif(basicsalary>20000):
    HRA=basicsalary*(30/100)
    print("Your HRA = ",HRA)
    DA=basicsalary*(95/100)
    print("Your DA = ",DA)
    c=basicsalary+HRA+DA
    print("Your total SALARY = ",c)
print("T  H  A  N  K  S  ")


#Q32. Write a python program to print n natural number using while loop.
number=int(input("Enter the number =  "))
i=1
print("The list of Natural numbers from 1 to {0} are".format(number))
while (i<=number):
    print(i,end= ' ')
    i=i+1


#Q33. Write a python program to print all odd numbers in a given range.

a=int(input("Plese Enter The Maximum Value :  "))
number=1
while number<=a:
    if (number%2!= 0):
        print("{0}".format(number))
    number=number+1


#Q34. Write a python program to add first n numbers using while loop.

num=int(input("Enter the number =  "))
sum=0
while(num>0):
    sum+=num
    num-=1
print("The total is = ",sum)


#Q35. Write a python program to print all numbers in a given range which are divisible by 3 or 5 using while loop.

a=int(input("Enter the Maximum Value :  "))
b=1
while b<=a:
    if (b%3==0 or b%5==0):
        print("{0}".format(b))
        b=b+1
    else:
        b=b+1


#Q36. Write a python program to count the number of even & odd numbers from a series of numbers using loop.

a=int(input("Enter the Maximum Value :  "))
n=1
odd,even=0,0
while n<=a:
    if(n%2==0):
        even=even+1
        n=n+1
    else:
        odd=odd+1
        n=n+1
print("This is a EVEN number = ",even)
print("This is a ODD number = ",odd)


#Q37. Write a python program to add all EVEN numbers in a given range.

num=int(input("Enter the starting range : "))
max=int(input("Enter the Ending range : "))
sum=0
while num<=max:
    if(num%2==0):
        sum=sum+num
        num=num+1
    else:
        num=num+1
print("The sum of the given range : ",sum)


#Q38. Write a python program to calculate the factorial of a given numbers using loop.

num=int(input("Enter the valuable Number : "))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    i=i+1
print("Factorial of ", num,"is", factorial)

#Q39. Write a python program to find if a number is prime or not.

number=int(input("Enter a number [GRATER THAN 1] = "))
f=0
i=2
while i<=number/2:
    if number%i==0:
        f=1
        break
    i=i+1
if f==0:
    print("This number is a PRIME number. ")
else:
    print("This number is not a PRIME number.")


#Q40. Write a python program to find the reverse of a given number.

number=int(input("Enter the valuable number : "))
reversed_num=0
while number!=0:
    digit=number%10
    reversed_num=reversed_num*10+digit
    number//=10
print("Reversed Number : "+str(reversed_num))


#Q41. Write a python program to add all the digits of a given number.

number=int(input("Enter the number :  "))
sum=0
while(number!=0):
    sum=sum+int(number%10)
    number=int(number/10)
print("The sum of DIGIT =  ",sum)


#Q42. Write a python program to print all the FIBONACCI series up to given range.

number=int(input("Enter the Value : "))
a=0
b=1
sum=0
count=0
print("FIBONACCI Series : ",end=' ')
while (count<=number):
    print(sum,end=' ')
    count+=1
    a=b
    b=sum
    sum=a+b


#Q43. Write a python program to find a number is ARMSTRONG or not.

number=int(input("Enter the Number =  "))
order=len(str(number))
temp=number;
sum=0
while (temp>0):
    digit=temp%10
    sum+=digit**order
    temp=temp//10
if(sum==number):
    print("This is an ARMSTRONG number = ",number)
else:
    print("This is not a ARMSTRONG number = ",number)


#Q44. Write a python program to find a number is PALINDROME or not.

number=int(input("Enter the valuable number = "))
reverse=0
numbers=number
while (number!=0):
    remainder=number%10
    reverse=reverse*10+remainder
    number=int(number/10)
if (numbers==reverse):
    print("This is a PALINDROME number = ",numbers)
else:
    print("This is not a PALINDROME number = ",numbers)


#Q45. Write a python program to check a number is PERFECT or not.

number=int(input("Enter the number = "))
i=1
sum=0
while(i<number):
    if(number%i==0):
        sum=sum+i
    i=i+1
if (sum==number):
    print("This is a PERFECT number = ",number)
else:
    print("This is not a PERFECT number = ",number)


#Q46. Write a python program to find out PRIME numbers with in 100

#   WHITIN 100

number=1
while(number<=100):
    count=0
    i=2
    while(i<=number//2):
        if(number%i==0):
            count=count+1
            break
        i=i+1
    if(count==0 and number!=1):
        print("%d"%number,end=' ')
    number=number+1

#   WHITIN GIVEN USERS RANGE

usersrange=int(input("Enter the RANGE = "))
number=1
while(number<=usersrange):
    count=0
    i=2
    while(i<=number//2):
        if(number%i==0):
            count=count+1
            break
        i=i+1
    if(count==0 and number!=1):
        print("%d"%number,end=' ')
    number=number+1


#Q47. Write a python program to print fibonacci number.

n=int(input("Enter the number= "))
a=0
b=1
sum=0
count=0
print("Fibonacci number : ",end=" ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b


#Q48. Write a python program to print a pattern.

n=int(input("Enter the number of rows= "))
for i in range (0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()


#Q49. Write a python program to reverse pattern printing.

n=int(input("Enter the number of rows: "))
while n>=0:
    print(n*"*")
    n=n-1


#Q50. Write a python program to check whether a number is prime or not using function.

def prime (num):
    count=0
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                count=count+1
    if count==0:
        print(num,"is the prime number.")
    else:
        print(num,"Is not a prime number.")
num=int(input("Enter  the number: "))
print("The number is: ",num)
prime (num)


#Q51. Write a python program to check if a number is a palindrome or not using function.

def check_palindrome(my_string):
    if len(my_string)<1:
        return True
    else:
        if my_string[0]==my_string[-1]:
            return check_palindrome(my_string[1:-1])
        else:
            return False
my_string=str(input("Enter the string: "))
print("The string is : ")
print(my_string)
if (check_palindrome(my_string)==True):
    print("This number is a palindrome.")
else:
    print("This is not a palindrome number.")


#Q52. Write a python program to calculate the factrial of a given number using function.

def factorial(num):
    if num==1:
        return 1
    else:
        return(num*factorial(num-1))
num=int(input("Enter the number: "))
result=factorial(num)
print("The factorial of",num,"is",result)

#Q53.Write a python program to calculate the fibonacci series using function.

def fibo(num):
    if num<=1:
        return num
    else:
        return (fibo(num-1)+fibo(num-2))
terms=int(input("Enter the number: "))
if terms<=0:
    print("Plese enter a positive integer.")
else:
    print("Fibonacci sequence: ")
    for i in range(terms):
        print(fibo(i))


#Q54. Write a python program to swap two numbers by call by value and call by address.

def swap(a,b):
    a,b=b,a
    print("Call by refferance",a,b)
a=int(input("Enter the value of a:  "))
b=int(input("Enter the value of b:  "))
swap(a,b)
print("Call by value: ", a,b)


#Q55. Write a python program to pring a pattern.

def pattern (rows):
    num=1
    for i in range(rows):
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print()
rows=int(input("Enter the value: "))
pattern(rows)

#Q56. write a python program to printing a * pattern.

def pattern(rows):
    for i in range(rows):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
rows=int(input("Enter the number of rows: "))
pattern(rows)


#Q57. Write a python program to  REverse printing a pattern.

def pattern(rows):
    for i in range(rows):
        for j in range(i,rows):
            print("*",end=" ")
        print()
rows=int(input("Enter the rows: "))
pattern(rows)

#Q58. Write a python program to printing a pattern.

def pattern(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print()
rows=int(input("Enter the number of rows: "))
pattern(rows)


#Q59. Write a python program to create a tuple.

#EMPTY TUPLE

tuple=()
print(tuple)

#TUPLE HAVING INTEGERS

tuple=(1,2,3)
print(tuple)

#TUPLE WITH MIXED DATATYPE

tuple=(1,"MANISH",4.55)
print(tuple)

#NESTED TUPLE

tuple=("BWU",[87],'@',78,(3,4,5,6))
print(tuple)


#Q60. Write a python program to create a tuple with different data type.

tuple=('Brainware university','Manish',6,2022)
print(tuple)


#Q61. Write a python program to unpack a tuple in several variables.

tuple=(24,7,10)
print(tuple)
n1,n2,n3=tuple
print(n1+n2+n3)


#Q62. Write a python program to add an item to a tuple.

tuple=(2,5,8)
tuple_append=tuple+(12,7,9,10)
print(tuple_append)


#Q63. Write a python program to convert a tuple to a string.

tuple=('B','R','A','I','N','W','A','R','E')
string= ''.join(tuple)
print(string)

#Q64. Write a python program to find a repeated items of a tuple.

tuple= 2,3,4,5,6,7,7,7,6
print(tuple)
count=tuple.count(4)
count2=tuple.count(6)
count3=tuple.count(7)
print("Number 4 repeated = ",count,"times.")
print("Number 6 repeated ",count2,"times.")
print("Number 7 repeated ",count3,"times.")

#Q65. Write a python program to convert a tuple to a dictionary.

tuple=((11,'eleven'),(21,'Milk'),(19,'Dist'),(6,'Manish'))
print(tuple)
dct=dict((x,y)for x,y in tuple)
print(dct)

#Q66. Write a python program that accepts a list from the user and prints the alternate element of the list.

#USING APPEND FUNCTION...................

my_list=[]
size=int(input("How many element you wants to want to enter:  "))
print("Enter",str(size),"elements")
for i in range(size):
    my_list.append(input())
print("The elements of list is: "+str(my_list))
print("Alternate elements are: ")
for i in range(0,size,2):
    print(my_list[i])


#Q67. Write a python program that accepts a list of users.Your program should reverse the content of the list and display it.Do nit use reverse()method.

#DO NOT USING reverse() FUNCTION................

my_list=input("Enter the value of list :  ")
a=my_list[::-1]
print("Reverse list is : ",a)

#USING reverse() FUNCTION............

my_list=["bwu",'manish',6,'giri']
my_list.reverse()
print("Reverse list is : "+str(my_list))


