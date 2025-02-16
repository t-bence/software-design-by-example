"""A tiny expression evaluator with variables."""

import json
import sys

class TLLException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"TLLException: {self.message}"
    
def check(condition: bool, message: str = "Error") -> None:
    """Check if condition is True, raise TLLException with message if not."""
    if not condition:
        raise TLLException(message)

def do_abs(env, args):
    check(len(args) == 1)
    val = do(env, args[0])
    return abs(val)

def do_add(env, args):
    check(len(args) == 2)
    left = do(env, args[0])
    right = do(env, args[1])
    return left + right

def do_get(env, args):
    check(len(args) == 1)
    check(isinstance(args[0], str))
    check(args[0] in env, f"Unknown variable {args[0]}")
    return env[args[0]]

def do_seq(env, args):
    check(len(args) > 0)
    for item in args:
        result = do(env, item)
    return result

def do_set(env, args):
    check(len(args) == 2)
    check(isinstance(args[0], str))
    value = do(env, args[1])
    env[args[0]] = value
    return value

def do_array(env, args):
    check(len(args) == 1)
    length = do(env, args[0])
    check(isinstance(length, int))
    return list(range(length))

def do_array_get(env, args):
    # args: ["alpha", 3] -- meaning get item 3 from array named alpha
    # usage: ["array_get", "alpha", 3]
    check(len(args) == 2)
    check(isinstance(args[0], str), "Array name must be str")
    index = do(env, args[1])
    check(isinstance(index, int), "Array index must be int")
    array = do_get(env, [args[0]])
    check(index < len(array), "Array index out of bounds")
    check(index >= 0, "Array index must not be negative")
    return array[index]

def do_array_set(env, args):
    # ["array_set", "alpha", index=3, value=4]
    check(len(args) == 3)
    check(isinstance(args[0], str), "Array name must be str")
    index = do(env, args[1])
    check(isinstance(index, int), "Array index must be int")
    array = do_get(env, [args[0]])
    value = do(env, args[2])
    check(isinstance(value, int), "Array value must be an integer")
    check(index < len(array), "Array index out of bounds")
    check(index >= 0, "Array index must not be negative")
    array[index] = value
    return value

def do_print(env, args):
    # ["print", "constant", [anything]]
    # args: ["constant", [expr]]
    check(len(args) == 2)
    check(isinstance(args[0], str))
    value = do(env, args[1])
    print(f"{args[0]}: {value}")

def do_repeat(env, args):
    check(len(args) == 2)
    check(isinstance(args[0], int), "Number of repetitions must be int")
    for _ in range(args[0]):
        do(env, args[1])

def do_if(env, args):
    check(len(args) == 3)
    if do(env, args[0]):
        do(env, args[1])
    else:
        do(env, args[2])

def do_leq(env, args):
    check(len(args) == 2)
    left = do(env, args[0])
    right = do(env, args[1])
    return left <= right


# [lookup]
OPS = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}
# [/lookup]

# [do]
def do(env, expr):
    # Integers evaluate to themselves.
    if isinstance(expr, int):
        return expr

    # Lists trigger function calls.
    check(isinstance(expr, list), "Argument must be list or int")
    check(expr[0] in OPS, f"Unknown operation {expr[0]}")
    func = OPS[expr[0]]
    return func(env, expr[1:])
# [/do]

def main():
    assert len(sys.argv) == 2, "Usage: interpreter.py filename"
    with open(sys.argv[1], "r") as reader:
        program = json.load(reader)
    try:
        result = do({}, program)
        print(f"=> {result}")
    except TLLException as e:
        print(e)


if __name__ == "__main__":
    main()
