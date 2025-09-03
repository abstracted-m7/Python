'''
    4. Implement the bubble sort algorithm in python.
    5. Show intermediate steps of each iteration.
    algo - 
        s1: Initialize n as the length of the array.
        s2: For i from 0 to n-1 (outer loop):
        s3: For j from 0 to n - i - 2 (inner loop):
        s4: Compare the element at index j with the element at index j + 1.
        s5: If arr[j] is greater than arr[j + 1], swap them.
        s6: After each inner loop pass, the largest unsorted element will be placed at index n - i - 1.
        s7: Repeat until all elements are sorted.
        s8: Return the sorted array.


'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element > next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"In {i}'th iteration: {arr}")
    return arr


arr = [6, 3, 5, 1, 2, 9]
print(f"Org array: {arr}")
print(f"Bubble Sort: {bubble_sort(arr)}")
