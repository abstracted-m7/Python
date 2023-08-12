#Evaluate with a function that takes in this array as an argument and returns the sum of all the elements that are located in the diagonals of the array
def sum_diagonal_elements(arr):
    rows = len(arr)
    cols = len(arr[0])
    diagonal_sum = 0

    # Sum elements in the main diagonal
    for i in range(min(rows, cols)):
        diagonal_sum += arr[i][i]

    # Sum elements in the secondary diagonal
    for i in range(rows):
        for j in range(cols):
            if i + j == rows - 1:
                diagonal_sum += arr[i][j]

    return diagonal_sum

# Example usage
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = sum_diagonal_elements(array)
print("The result is = ", result)