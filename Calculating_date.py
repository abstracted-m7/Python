# Write a program that reads a string from the user countaining a date in the from mm/dd/yyyy.It should print the date in the from of March 12,2021


months={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "Mey":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12,
    }

import re
for date in ['March 12,2021',-1]:
    if date==-1:
        break
    if re.match('(\w+)(\d{1,2})',date)==None:
        continue
    output=date.split("")
    output[0]=str(months[output[0]])
    output[1]=output[1].replace(","," ")
    print("/".join(output))
