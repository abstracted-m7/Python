# Bubble Sort vs Selection Sort: Performance and Iteration Count Comparison

# Bubble Sort:
# - Iteration behavior:
#   In each pass through the list, adjacent elements are compared and swapped if they are in the wrong order.
#   The largest unsorted element "bubbles up" to its correct position at the end.
# - Number of passes:
#   Typically requires (n-1) passes through the array for n elements.
# - Inner loop:
#   For each pass i, the inner loop runs (n - 1 - i) times, because the last i elements are already sorted.
# - Comparisons:
#   Approximately n*(n-1)/2 comparisons in worst and average case.
# - Swaps:
#   Can be as high as n*(n-1)/2 swaps in worst case (if array is reverse sorted).
# - Early stopping:
#   Can be optimized with a swapped flag to stop if no swaps happened during a pass (best case O(n)).

# Selection Sort:
# - Iteration behavior:
#   In each pass, the algorithm selects the minimum element from the unsorted part and swaps it with the first unsorted element.
# - Number of passes:
#   Always (n-1) passes through the array.
# - Inner loop:
#   For each pass i, the inner loop runs (n - i) times to find the minimum element.
# - Comparisons:
#   Always n*(n-1)/2 comparisons regardless of initial order (no early stopping).
# - Swaps:
#   Exactly (n-1) swaps, as only one swap per pass is performed.
# - Best case and worst case complexity are the same since selection sort always performs the same comparisons.

# Summary:
# - Bubble Sort may perform fewer swaps if the list is nearly sorted, due to early stopping optimization.
# - Selection Sort performs fewer swaps overall but does not benefit from early stopping.
# - Both have average and worst time complexities of O(n^2).
# - Bubble Sort's iteration count per pass decreases with each pass due to the sorted tail.
# - Selection Sort always iterates through the entire unsorted portion each pass.

# Therefore:
# - Bubble Sort may be faster on nearly sorted arrays.
# - Selection Sort performs a predictable number of swaps, which might be better when swap cost is high.
