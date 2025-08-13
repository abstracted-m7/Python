def num_senti(num):
    if num == 0:
        return "zero"
    elif num < 0:
        return "neg"
    elif num > 0:
        return "pos"
    else:
        return "Enter valid number"

print(num_senti(0))