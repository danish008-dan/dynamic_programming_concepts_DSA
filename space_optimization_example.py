"""
Purpose:
--------
Demonstrate Space Optimization in Dynamic Programming
using the Fibonacci problem.

This approach reduces space usage by storing only
the required previous states instead of a full DP table.
"""

def fibonacci_space_optimized(n):
    # Handle base cases
    if n <= 1:
        return n

    prev2 = 0  # F(0)
    prev1 = 1  # F(1)

    # Compute Fibonacci using constant space
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


print("Fibonacci (Space Optimized):", fibonacci_space_optimized(10))
