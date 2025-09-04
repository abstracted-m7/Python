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

def ordinal(n):
    # Helper to get ordinal suffix for a number
    return "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"After {ordinal(i + 1)} iteration: {arr}")
    return arr

def main():
    user_input = input("Enter numbers separated by spaces: ")
    try:
        arr = list(map(int, user_input.split()))
    except ValueError:
        print("Please enter valid integers only.")
        return

    print(f"Original array: {arr}")
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
