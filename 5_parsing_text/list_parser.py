from string import digits
from typing import Any

def parse(input: str):

    def tok(text: str) -> list:
        number = ""
        result = []
        for ch in text:
            if ch in digits:
                number += ch
            elif ch == ",": # a number ends here
                result.append(int(number))
                number = ""
            elif ch in ("[", "]"):
                result.append(ch)
            elif ch == " ":
                pass
            else:
                raise ValueError("Unexpected character")
        if number:
            result.append(int(number))
        return result
    
    tokens = tok(input)

    def rindex(start, end, char):
        lst = tokens[start:end] if end else tokens[start:]
        return len(lst) - 1 - lst[::-1].index(char)

    def _parse(start: int = 0, end: int = None) -> list:
        result = []
        if end is not None and start >= end:
            return result
        elif end == len(tokens):
            return result
        elif isinstance(tokens[start], int):
            result.append(tokens[start])
            result.append(_parse(start + 1, end))
        elif tokens[start] == "[":
            closing_index = rindex(start, end, "]")
            result.append(_parse(start + 1, closing_index-1))
            result.append(_parse(closing_index + 1))
        else:
            raise ValueError(start, end, tokens[start])

    return _parse()

if __name__ == "__main__":
    print(parse("[1, [2, [3, 4], 5]]"))