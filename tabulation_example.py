"""
Purpose:
--------
Demonstrate Tabulation (Bottom-Up Dynamic Programming)
using the Fibonacci problem.

Tabulation builds the solution iteratively from
base cases to the final answer.
"""

def fib_tabulation(n):
    # Handle base cases
    if n <= 1:
        return n

    # Create DP table
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 0
    dp[1] = 1

    # Build table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("Fibonacci using Tabulation:", fib_tabulation(10))
