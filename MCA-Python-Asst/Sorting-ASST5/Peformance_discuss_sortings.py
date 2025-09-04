# 8. Discuss performance or iteration count differences in comments.


# Bubble Sort:
# - Iterations: Up to (n-1) passes; inner loop runs (n-1-i) times per pass
# - Comparisons: ~n*(n-1)/2
# - Swaps: Up to ~n*(n-1)/2 in worst case
# - Time Complexity: O(n²) worst & average, O(n) best (if optimized with early stop)
# - Space Complexity: O(1) (in-place)
# - Notes: Can stop early if no swaps in a pass (efficient for nearly sorted lists)

# Selection Sort:
# - Iterations: Always (n-1) passes; inner loop runs (n-i) times per pass
# - Comparisons: Always n*(n-1)/2 (no early stopping)
# - Swaps: Exactly (n-1)
# - Time Complexity: O(n²) in all cases
# - Space Complexity: O(1) (in-place)
# - Notes: Fewer swaps than Bubble Sort; predictable behavior regardless of input order

