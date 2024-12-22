# Matching patterns

## Task 1 - Looping

> Rewrite the matchers so that a top-level object manages a list of matchers, none of which know about any of the others. Is this design simpler or more complicated than the Chain of Responsibility design?

TODO

## Length plus one

> Why does the upper bound of the loop in the final version of Any run to len(text) + 1?

Because `range(a, b)` goes only up to `b-1`.

## Find One or More

> Extend the regular expression matcher to support +, meaning “match one or more characters”.

## Match Sets of Characters

> Add a new matching class that matches any character from a set, so that Charset('aeiou') matches any lower-case vowel.
> Create a matcher that matches a range of characters. For example, Range("a", "z") matches any single lower-case Latin alphabetic character. (This is just a convenience matcher: ranges can always be spelled out in full.)
> Write some tests for your matchers.

## Exclusion

> Create a matcher that doesn’t match a specified pattern. For example, Not(Lit("abc")) only succeeds if the text isn’t “abc”.
> Write some tests for it.

## Make Repetition More Efficient

> Rewrite Any so that it does not repeatedly re-match text.

## Multiple Alternatives

> Modify Either so that it can match any number of sub-patterns, not just two.
> Write some tests for it.
> What does your implementation do when no sub-patterns are specified?

## Returning Matches

> Modify the matcher so that it returns the substrings that matched each part of the expression. For example, when *.txt matches name.txt, the library should return some indication that * matched the string "name".

## Alternative Matching

> The tool we have built implements lazy matching, i.e., the * character matches the shortest string it can that results in the overall pattern matching. Modify the code to do greedy matching instead, and combine it with the solution to the previous exercise for testing.
