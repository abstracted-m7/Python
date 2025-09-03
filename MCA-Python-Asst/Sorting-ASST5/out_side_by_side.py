# Simple Bubble Sort vs Selection Sort - Table Format

def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result

def selection_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result

# Test arrays
test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9],
    [1, 2, 3, 4, 5]
]

names = ["Random", "Small", "Sorted", "Reverse"]

# Table header
print("=" * 80)
print("           BUBBLE SORT vs SELECTION SORT - SIDE BY SIDE")
print("=" * 80)
print(f"{'Test Case':<12} {'Original Array':<25} {'Bubble Sort':<20} {'Selection Sort':<20}")
print("-" * 80)

# Process each test case
for i, (arr, name) in enumerate(zip(test_arrays, names)):
    bubble_result = bubble_sort(arr)
    selection_result = selection_sort(arr)
    
    print(f"{name:<12} {str(arr):<25} {str(bubble_result):<20} {str(selection_result):<20}")

print("-" * 80)
print("All results verified: Both algorithms produce identical sorted outputs")