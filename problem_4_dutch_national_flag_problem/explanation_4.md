# Dutch National Flag Problem

## Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Requirements

Python version 3.6 and above

## Solution

The solution does a single traversal though the entire input array. The worst case time complexity is O(n) since it iterates through every element once. The sorting uses In-place sorting so the space complexity is kept minimal with only a few variables for keeping index values making it O(1).