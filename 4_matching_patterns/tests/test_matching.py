from patterns import *

def test_lit():
    assert Lit("abc").match("abc")

    assert not Lit("abc").match("def")
    
    matcher = Lit("abc", Lit("def"))
    assert matcher.match("abcdef")

    # pytest.raises(Lit("abc").match, "def")

def test_any():
    assert Any().match("abc")
    assert Any().match("")

    assert Any(Lit("abc")).match("abc")
    assert Any(Lit("abc")).match("xyzabc")

def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")

def test_either_two_literals_not_both():
    # /{a,b}/ doesn't match "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")

def test_either_followed_by_literal_match():
    # /{a,b}c/ matches "ac"
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")

def test_either_followed_by_literal_no_match():
    # /{a,b}c/ doesn't match "ax"
    assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")

def test_either_followed_by_literal_matches():
    # /{a,b}c{a,b}/ matches "aca"
    assert Either(Lit("a"), Lit("b"), Lit("c", Either(Lit("a"), Lit("b")))).match("aca")

def test_plus():
    assert Plus().match("a")
    assert Plus().match("abc")
    assert not Plus().match("")

    assert not Plus(Lit("abc")).match("abc")
    assert Plus(Lit("abc")).match("xabc")
    assert Plus(Lit("abc")).match("xyzabc")

def test_charset():
    assert Charset("abcd").match("a")
    assert not Charset("abcd").match("x")
    assert Charset("abcd", Any()).match("abc")

def test_range():
    assert Range("a", "d").match("a")
    assert not Range("a", "d").match("x")
    assert Range("a", "d", Any()).match("abc")
