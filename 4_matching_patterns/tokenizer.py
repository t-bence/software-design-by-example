import string

CHARS = set(string.ascii_letters + string.digits)

class Tokenizer:
    def __init__(self):
        self._setup()

    def _setup(self):
        self.result = []
        self.current = ""
        self.escaped = False

    def tok(self, text):
        self._setup()
        for ch in text:
            if self.escaped:
                self.current += ch
                self.escaped = False
            else:
                match ch:
                    case "": self._add(None)
                    case "*": self._add("Any")
                    case "{": self._add("EitherStart")
                    case ",": self._add(None)
                    case "}": self._add("EitherEnd")
                    case "[": self._add("CharsetStart")
                    case "]": self._add("CharsetEnd")
                    case "!": self._add("Not")
                    case ch if ch in CHARS: self.current += ch
                    case "\\": self.escaped = True
                    case _: raise NotImplementedError(f"what is '{ch}'?")
        self._add(None)
        return self.result

    def _add(self, thing):
        if len(self.current) > 0:
            self.result.append(["Lit", self.current])
            self.current = ""
        if thing is not None:
            self.result.append([thing])
