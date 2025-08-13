def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return year
    else:
        return find_next_year(year)

def find_next_year(year):
    return year + 1

start_year = 2001
next_year = find_next_year(start_year)
print(f"The next leap year after {start_year} is {next_year}")

