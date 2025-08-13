# def num_senti(num):
#     if num == 0:
#         return "zero"
#     elif num < 0:
#         return "neg"
#     elif num > 0:
#         return "pos"
#     else:
#         return "Enter valid number"

# print(num_senti(0))



def num_senti(num):
    try:
        num_float = float(num)
        if num_float == 0:
            return "Zero"
        elif num_float < 0:
            return "Negative"
        elif num_float > 0:
            return "Positive"
    except ValueError:
        return "Please enter a valid number."


user_input = input("Enter a number: ")
print(num_senti(user_input))

