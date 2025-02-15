import datetime as dt
from pprint import pprint
import argparse

import tests

def test_unity():
    assert 1 == 1

def test_fails():
    assert 1 == 2

def test_errors():
    assert 1 == int("alma")

def run_tests(pattern: str = "test") -> None:
    passed = []
    failed = []
    errored = []
    
    test_functions = [func for name, func in globals().items()
                if name.startswith(pattern) and callable(func)]
    
    import inspect
    test_modules = [module for name, module in globals().items()
        if name.startswith(pattern) and inspect.ismodule(module)]
    for module in test_modules:
        for name in dir(module):
            if name.startswith(pattern):
                obj = getattr(module, name)
                if callable(obj):
                    test_functions.append(obj)

    for func in test_functions:
        try:
            func()
            passed.append(func.__name__)
        except AssertionError:
            failed.append(func.__name__)
        except:
            errored.append(func.__name__)

    print(f"Collected: {len(test_functions)}")
    print(f"Passed: {len(passed)} ({', '.join(passed)})")
    print(f"Failed: {len(failed)} ({', '.join(failed)})")
    print(f"Errored: {len(errored)} ({', '.join(errored)})")


def main():
    parser = argparse.ArgumentParser(description="Run unit tests.")
    parser.add_argument('-p', '--pattern', type=str, help='Pattern to match test function names', default='test')
    args = parser.parse_args()
    pattern = args.pattern

    run_tests(pattern)

if __name__ == "__main__":
    main()
    #pprint(globals())

    #t = dir(globals()['tests'])[-1]
    #getattr(tests, t)()
    