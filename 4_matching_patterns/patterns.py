from abc import ABC

class Match(ABC):
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()
    
    def match(self, text):
        result = self._match(text, 0)
        return result == len(text)

    def _match(self, text, start):
        raise NotImplementedError()
    
    def __eq__(self, other):
        return (other is not None and 
                self.__class__ == other.__class__ and 
                self.rest == other.rest)

class Lit(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text, start):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
    
    def __eq__(self, other):
        return super().__eq__(other) and (
            self.chars == other.chars
        )


class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start):
        if self.rest is Null:
            return len(text)
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None
    

class Either(Match):
    def __init__(self, patterns, rest=None):
        super().__init__(rest)
        self.patterns = patterns

    def _match(self, text: str, start:int=0):
        for pattern in (self.patterns):
            end = pattern._match(text, start)
            if end is not None:
                return self.rest._match(text, end)
        return None
    
    def __eq__(self, other):
        return super().__eq__(other) and self.patterns.__eq__(
            other.patterns
        )


class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        return start


class Plus(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _match(self, text, start):
        for i in range(start + 1, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None


class Charset(Match):
    def __init__(self, chars: str, rest=None):
        super().__init__(rest)
        self.chars = tuple(chars)

    def _match(self, text, start):
        if start >= len(text):
            return None
        if text[start] in self.chars:
            return self.rest._match(text, start + 1)
        return None


class Range(Charset):
    def __init__(self, first:str, last:str, rest=None):
        # generate all characters between first and last
        chars = "".join(chr(c) for c in range(ord(first), ord(last) + 1))
        super().__init__(chars, rest)


class Not(Match):
    def __init__(self, pattern, rest=None):
        super().__init__(rest)
        self.pattern = pattern
    
    def _match(self, text, start):
        return self.pattern._match(text, start) != len(text)
