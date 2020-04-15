# Finding the Square Root of an Integer

## Problem

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

## Requirements

Python version 3.6 and above

## Solution

The space complexity of this solution is O(1) since it uses only 4 variables to keep track of the values. The time complexity is O(logn) as the algorithm removes half the list of numbers to check in every iteration.
