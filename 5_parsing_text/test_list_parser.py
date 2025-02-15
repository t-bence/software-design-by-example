from list_parser import parse

def test_list_parser():
    assert parse("[1, [2, [3, 4], 5]]") == [1, [2, [3, 4], 5]]

def test_list_parser_large_integers():
    assert parse("[10, [20, [30, 40], 50]]") == [10, [20, [30, 40], 50]]

def test_list_parser_consecutive_numbers():
    assert parse("[1, 2, 3, 4, [5, [6, 7], 8]]") == [1, 2, 3, 4, [5, [6, 7], 8]]
