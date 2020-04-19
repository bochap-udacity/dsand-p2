# HTTPRouter using a Trie

## Problem

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

## Requirements

Python version 3.6 and above

## Solution

The solution performs different operations namely inserting a new path. Finding a path handler using the absolute path.

Insert: operation is O(n) where n is the number of path parts in the absolute path
Find: operation is also O(n) where n is the number of path parts in the absolute path

So the worst case complexity of the trie is O(n).
Space complexity is worst case of O(n x m) where n is the number of path parts in the longest absolute path and n is the number of unique paths in the trie.
