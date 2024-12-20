# Finding duplicate files

## Task 1 - Odds of collision

With two bits, there are 4 possible values. The chance of not colliding is therefore 75% for the first two files. Then, 0.75^2 for three files and 0.75^3 for four files, which is 0.42, therefore the odds of colliding are 58%.

## Task 2 - Streaming I/O

_A streaming API delivers data one piece at a time rather than all at once. Read the documentation for the update method of hashing objects in Python’s hashing module and rewrite the duplicate finder from this chapter to use it._

