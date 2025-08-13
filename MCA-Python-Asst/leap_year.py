def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

start_year = int(input("Enter a year: "))

if is_leap_year(start_year):
    print(f"{start_year} is a leap year")
else:
    print(f"{start_year} is not a leap year")
    next_leap = find_next_leap_year(start_year)
    print(f"The next leap year after {start_year} is {next_leap}")
