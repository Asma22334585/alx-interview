#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    x = 0
    y = 2
    while n > 1:
        while not n % y:
            x += y
            n /= y
        y += 1
    return x
