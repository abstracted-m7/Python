'''
    1. Implementation the selection sort algorithm in python
    2. Display the selection and swapping process clearly.
    
    algo - 
        s1: Initialize the length of the array as n.
        s2: For i from 0 to n - 2 do:
        s3: Set min_idx = i (index of the minimum element).
        s4: For j from i + 1 to n - 1 do:
        s5: If arr[j] < arr[min_idx] then update min_idx = j.
        s6: If min_idx is not equal to i, swap arr[i] and arr[min_idx].
        s7: Repeat steps 2 to 4 until the entire array is sorted.
        s8: Return the sorted array.

'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"In {i}'th iteration: {arr}")
    return arr


arr = [1, 3, 5, 6, 2, 9]
print(f"Org array: {arr}")
print("Selection Sort:", selection_sort(arr))
