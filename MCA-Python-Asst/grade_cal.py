
def stud_grade(num):
    if num > 85:
        return "A grade"
    elif 75 <= num <= 85:
        return "B grade"
    elif 50 <= num < 75:
        return "C grade"
    elif 30 <= num < 50:
        return "D grade"
    else:
        return "Fail"

print(stud_grade(50))