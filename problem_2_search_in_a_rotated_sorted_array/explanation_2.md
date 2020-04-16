# Search in a Rotated Sorted Array

## Problem

You are given a sorted array which is rotated at some random pivot point.

Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example:

Input: `nums` = `[4,5,6,7,0,1,2]`, `target` = `0`, `Output`: `4`

## Requirements

Python version 3.6 and above

## Solution

This solution is broken into 2 parts. The first part identifies the 2 boundaries of the sequential range of numbers created by the array rotation. It makes use of the characteristic that the array is sorted and wraps from the end to the start due to the rotation. The second part searches for the number from the range of number boundaries.

In part 1, the use a similar concept that binary search uses to drop elements from the boundaries to decide the start and end index of the left and right boundaries with a runtime of O(log n) perform twice. In part 2, the number being searched is compared to the upper and lower limits of the left and right boundaries removing one of the boundaries using an O(1) operation. Then it uses binary search which is O(log n) to locate the number to be search. So the overall complexity of O(log n).

The solution only requires 4 variables to store the indexes of the upper and lower limit of the boundaries making the space complexity O(1).
