# Title: Fibonacci Series and Golden Ratio
# Author: Rushikesh Padaki
# Date: 24 May 2025
#
# Description:
# A Python program to generate the Fibonacci sequence up to n terms and compute the golden ratio.
#
# Fibonacci Sequence:
# - The Fibonacci sequence is a series where each number is the sum of the two preceding ones.
# - The sequence starts with 0 and 1 and follows the rule: F(n) = F(n-1) + F(n-2).
#
# Golden Ratio:
# - The golden ratio, denoted by the Greek letter φ (phi), is an irrational number approximately equal to 1.6180339887.
# - It is defined algebraically as the positive solution to the equation: φ = (1 + √5) / 2.
# - Geometrically, two quantities a and b (a > b > 0) are in the golden ratio if: (a + b) / a = a / b = φ.
# - This ratio is found in art, architecture, nature (e.g., spirals of shells and galaxies), and design due to its aesthetically pleasing properties.
#
# Relation to Fibonacci:
# - The ratio of successive Fibonacci numbers approximates the golden ratio.
# - As the Fibonacci sequence progresses, the ratio F(n)/F(n-1) converges to φ.
#
# Algorithm:
# 1. Take input `n` — number of terms of the Fibonacci series to generate.
# 2. Initialize the Fibonacci series list with the first two terms: [0, 1].
# 3. Generate the next terms by summing the last two values.
# 4. Calculate the golden ratio values as: fib[i] / fib[i-1] for i in range(2, n).
# 5. Print both the Fibonacci series and the golden ratio values.
#
# Time Complexity:
# - O(n) — Linear time to compute the series and ratios.
#
# Space Complexity:
# - O(n) — Additional space to store Fibonacci terms and golden ratio values.
#
# Sample Execution:
#
# Case 1:
# Input:
# Enter the number of terms to be generated for Fibonacci series: 10
# Output:
# Fibonacci series:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Golden ratio:  [1.0, 2.0, 1.5, 1.66667, 1.6, 1.625, 1.61538, 1.61905, 1.61905]

n = int(input('Enter the number of terms to be generated for Fibonacci series: '))

fibList = [0, 1]
for i in range(2, n):
    fibList.append(fibList[i - 1] + fibList[i - 2])

print('Fibonacci series: ', fibList)

# Calculate golden ratios, rounded to 5 decimal places
goldenRatio = [round(fibList[i] / fibList[i - 1], 5) for i in range(2, len(fibList))]

print('Golden ratio: ', goldenRatio)
