"""
Purpose:
--------
Demonstrate Memoization (Top-Down Dynamic Programming)
using the Fibonacci problem to avoid repeated calculations.
"""

def fib_memo(n, memo):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n

    # If result already computed, return it
    if n in memo:
        return memo[n]

    # Store the computed result in memo dictionary
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


memo = {}
print("Fibonacci using Memoization:", fib_memo(10, memo))
