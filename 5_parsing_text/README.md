# Parsing text

The solutions for this part are in the previous one, as they are closely related.

## Escape Characters

> Modify the parser to handle escape characters, so that (for example) \* is interpreted as a literal ‘*’ character and \\ is interpreted as a literal backslash.

This is done simply by adding a bool `escaped` attribute to the `Tokenizer` class. If it is true, no matter what the next character is, keep it in a `Lit`. Otherwise, do as previously (which I have rewritten to use `match` ... `case` syntax.)

## Character Sets

> Modify the parser so that expressions like [xyz] are interpreted to mean “match any one of those three characters”. (Note that this is a shorthand for {x,y,z}.)

So, it needs to create a `Charset` from whatever is between the square brackets.

## Negation

> Modify the parser so that [!abc] is interpreted as “match anything except one of those three characters”.

I wrote this using pattern matching, which was very handy and natural here. I also re-implemented the whole `Either` parsing with pattern matching, which feels a bit forced, but let me learn more about it.

## Nested Lists

> Write a function that accepts a string representing nested lists containing numbers and returns the actual list. For example, the input [1, [2, [3, 4], 5]] should produce the corresponding Python list.

This I will do here in this folder.

## Simple Arithmetic

> Write a function that accepts a string consisting of numbers and the basic arithmetic operations +, -, *, and /, and produces a nested structure showing the operations in the correct order. For example, 1 + 2 * 3 should produce ["+", 1, ["*", 2, 3]].
