from tokenizer import Tokenizer
from patterns import Any, Either, Lit, Null, Charset, Not

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
        match front[0]:
            case "Any": handler = self._parse_Any
            case "EitherStart": handler = self._parse_EitherStart
            case "Lit": handler = self._parse_Lit
            case "CharsetStart": handler = self._parse_CharsetStart
            case _: raise NotImplementedError(f"Unknown token type {front}")

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
    
    def _parse_CharsetStart(self, rest, back):
        negated = False
        if back[0][0] == "Not":
            negated = True
            back = back[1:]
        lit, chars = back[0]
        if lit != "Lit" and back[1][0] != "CharsetEnd":
            raise ValueError("badly-formatted Charset")

        if negated:
            return Not(Charset(chars, self._parse(back[2:])))
        else:
            return Charset(chars, self._parse(back[2:]))

if __name__ == "__main__":
    Parser().parse("[!xyz]")