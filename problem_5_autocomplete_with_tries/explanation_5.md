# Building a Trie in Python

## Problem

A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

## Requirements

Python version 3.6 and above

## Solution

The solution performs different operations namely inserting a new word. Finding a node based on its prefix and gathering suffixes.

Insert: operation is O(n) where n is the number of characters in the word
Find: operation is also O(n) where n is the number of characters in the prefix to be search
Suffixes: operation is also O(n x k) where n is the number of characters in the longest word to be suffixed and k is the number of children in the node to obtain the suffix.

So the worst case complexity of the trie is O(n x k).
Space complexity is worst case of O(n x k) where n is the number of characters in the longest string and k is the number of unique words in the trie.