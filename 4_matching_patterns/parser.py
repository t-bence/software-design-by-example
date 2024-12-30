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
        lits = []
        while back:
            match back:
                case [["Lit", chars], *rest]:
                    lits.append(Lit(chars))
                    back = rest
                case [["EitherEnd"], *rest]:
                    return Either(lits, self._parse(rest))
                case _:
                    raise ValueError("Badly-formatted Either")

    def _parse_CharsetStart(self, rest, back):
        match back:
            case [["Not"], ["Lit", chars], ["CharsetEnd"], *rest]:
                return Not(Charset(chars), self._parse(rest))
            case [["Lit", chars], ["CharsetEnd"], *rest]:
                return Charset(chars, self._parse(rest))
            case _:
                raise ValueError("badly-formatted Charset")

if __name__ == "__main__":
    Parser().parse("{abc,def}")