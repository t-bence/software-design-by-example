from abc import ABC



class Match(ABC):    
    def match(self, text: str):
        raise NotImplementedError()

class Lit(Match):
    def __init__(self, chars):
        self.chars = chars

    def match(self, text: str):
        if text[0:len(self.chars)] == self.chars:
            return len(self.chars)
        return None


class Any(Match):
    def match(self, text: str):
        return len(text)
    

class Either(Match):
    def __init__(self, patterns: tuple[Match]):
        self.patterns = patterns

    def match(self, text: str):
        for pattern in (self.patterns):
            end = pattern.match(text)
            if end is not None:
                return self.rest._match(text, end)
        return None


class Plus(Match):
    def match(self, text: str):
        if len(text) == 0:
            return None
        return len(text)


class Charset(Match):
    def __init__(self, chars: str):
        self.chars = tuple(chars)

    def match(self, text: str):
        if len(text) != 1:
            return None
        if text[0] in self.chars:
            return 1
        return None


class Range(Charset):
    def __init__(self, first:str, last:str, rest=None):
        # generate all characters between first and last
        chars = "".join(chr(c) for c in range(ord(first), ord(last) + 1))
        super().__init__(chars, rest)


class Not(Match):
    def __init__(self, pattern):
        self.pattern = pattern
    
    def match(self, text):
        return self.pattern.match(text) != len(text)
    

class PatternManager:
    def __init__(self, *patterns: list[Match]):
        self.patterns = patterns

    def match(self, input: str):
        start = 0
        for pattern in self.patterns:
            if isinstance(pattern, Any):
                pass
            matched = pattern.match(input[start:])
            if matched is None:
                return False
            start += matched
        return start == len(input)
