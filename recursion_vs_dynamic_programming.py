"""
Purpose:
--------
This file demonstrates the difference between Recursion
and Dynamic Programming using the Fibonacci problem.

It explains why recursion is inefficient and how DP
optimizes the solution.
"""

# -----------------------------
# Recursive Approach
# -----------------------------

def fib_recursive(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n

    # Recursive calls (repeated subproblems)
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# -----------------------------
# Dynamic Programming Approach
# -----------------------------

def fib_dp(n):
    # Create a DP array to store results
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    if n > 0:
        dp[1] = 1

    # Fill the DP table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("Recursive Fibonacci:", fib_recursive(6))
print("DP Fibonacci:", fib_dp(6))
