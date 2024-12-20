# Finding duplicate files

## Task 1 - Odds of collision

With two bits, there are 4 possible values. The chance of not colliding is therefore 75% for the first two files. Then, 0.75^2 for three files and 0.75^3 for four files, which is 0.42, therefore the odds of colliding are 58%.

## Task 2 - Streaming I/O

_A streaming API delivers data one piece at a time rather than all at once. Read the documentation for the update method of hashing objects in Python’s hashing module and rewrite the duplicate finder from this chapter to use it._

This was really simple.

## Task 3 - Big Oh

That case is N(N-1), so effectively O(N^2).

## Task 4 - `hash` function

It cannot hash mutable values, that is why it fails for `hash([1, 2, 3])`.

## Task 5 - How good is SHA-256?

1. Write a function that calculates the SHA-256 hash code of each unique line of a text file.
1. Convert the hex digests of those hash codes to integers.
1. Plot a histogram of those integer values with 20 bins.
1. How evenly distributed are the hash codes? How does the distribution change as you process larger files?

I will do this in another file, `plotting_sha.py`.

Looks simple, but now the plotting fails because the numbers are too large. So, I added modulo 1_000_000 to that.
