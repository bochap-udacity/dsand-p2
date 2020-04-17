# Rearrange Array Elements

## Problem

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Requirements

Python version 3.6 and above

## Solution

The solution is broken into 2 parts. Part 1 involves sorting the input which has a complexity of O(n log n) to get the elements in a descending order. Part 2 involves taking sorted input and iterating through all elements to obtain the integer outputs. This make the worst case complexity O(n log n). The space complexity is O(1) since only 2 integers is required to store the output.
