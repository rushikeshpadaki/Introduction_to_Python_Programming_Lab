# Title: Largest Prime Factor of a Number
# Author: Rushikesh Padaki
# Date: 23 May 2025
#
# Description:
# A Python program to compute the largest prime factor of a user-entered number.
# - Handles both even and odd prime factors efficiently.
# - Optimized by checking only up to the square root of the number.
#
# Algorithm:
# 1. Take an integer input n from the user.
# 2. While n is divisible by 2:
#    - Set maxPrime to 2 and divide n by 2.
# 3. Loop through odd numbers i from 3 to √n:
#    - While n is divisible by i:
#        - Set maxPrime to i and divide n by i.
# 4. If n is still greater than 2, it is itself a prime factor.
# 5. Print maxPrime as the largest prime factor.
#
# Time Complexity:
# - O(√n) — Efficient trial division up to square root of n.
#
# Space Complexity:
# - O(1) — Only a few variables used; constant space.
#
# Sample Execution:
#
# Case 1: Input is 13195
# Input:
# Enter a number: 13195
# Output:
# Largest prime factor: 29
#
# Case 2: Input is 49
# Input:
# Enter a number: 49
# Output:
# Largest prime factor: 7

n = int(input("Enter a number: "))
maxPrime = -1

# Divide out all factors of 2
while n % 2 == 0:
    maxPrime = 2
    n = n // 2

# Divide out odd factors
for i in range(3, int(n ** 0.5) + 1, 2):
    while n % i == 0:
        maxPrime = i
        n = n // i

# If remaining n is a prime number > 2
if n > 2:
    maxPrime = n

print('Largest prime factor:', int(maxPrime))
