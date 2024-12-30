from tokenizer import Tokenizer
from patterns import Any, Either, Lit, Null

class Parser:
    def parse(self, text):
        tokens = Tokenizer().tok(text)
        return self._parse(tokens)

    def _parse_Any(self, rest, back):
        return Any(self._parse(back))

    def _parse_Lit(self, rest, back):
        return Lit(rest[0], self._parse(back))

    def _parse(self, tokens):
        if not tokens:
            return Null()

        front, back = tokens[0], tokens[1:]
        if front[0] == "Any": handler = self._parse_Any
        elif front[0] == "EitherStart": handler = self._parse_EitherStart
        elif front[0] == "Lit": handler = self._parse_Lit
        else:
            assert False, f"Unknown token type {front}"

        return handler(front[1:], back)

    def _parse_EitherStart(self, rest, back):
        children = []
        while back and (back[0][0] == "Lit"):
            children.append(Lit(back[0][1]))
            back = back[1:]

        if not children:
            raise ValueError("empty Either")

        if back[0][0] != "EitherEnd":
            raise ValueError("badly-formatted Either")

        return Either(children, self._parse(back[1:]))
