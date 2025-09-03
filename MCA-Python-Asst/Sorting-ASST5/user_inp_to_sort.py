'''
    3. Allow user input for the list to be sorted.
    
    
    algo - 
        s1: Take user input in string.
        s2: Convert the input string into a list of numbers.
        s3: Use Bubble Sort to sort the list:
                s3.1: performe loop in the list. [i -> n & j -> (0, n-i-1)]
                s3.2: Compare each elements(n[j] > n[j+1]).
                s3.3: Swap them if they are in the wrong order.

        s4: Output the sorted list.
'''


# Step 1: Take user input as a string
user_input = input("Enter numbers x y: ")

# Step 2: Convert string list into int
num_list = list(map(int, user_input.split()))

# Step 3: Bubble Sort implementation
n = len(num_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if num_list[j] > num_list[j + 1]:
            # Swaping
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

# Step 4: Print the sorted list
print("Sorted list:", num_list)
