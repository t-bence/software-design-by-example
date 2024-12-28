from patterns import *

def test_lit():
    assert PatternManager(Lit("abc")).match("abc")

    assert not PatternManager(Lit("abc")).match("def")
    
    assert PatternManager(Lit("abc"), Lit("def")).match("abcdef")

    # pytest.raises(Lit("abc").match, "def")

def test_any():
    assert PatternManager(Any()).match("abc")
    assert PatternManager(Any()).match("")

    assert PatternManager(Any(), Lit("abc")).match("abc")
    assert PatternManager(Any(), Lit("abc")).match("xyzabc")

def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either((Lit("a"), Lit("b"))).match("a")

def test_either_two_literals_not_both():
    # /{a,b}/ doesn't match "ab"
    assert not Either((Lit("a"), Lit("b"))).match("ab")

def test_either_followed_by_literal_match():
    # /{a,b}c/ matches "ac"
    assert Either((Lit("a"), Lit("b")), Lit("c")).match("ac")

def test_either_followed_by_literal_no_match():
    # /{a,b}c/ doesn't match "ax"
    assert not Either((Lit("a"), Lit("b")), Lit("c")).match("ax")

def test_either_followed_by_literal_matches():
    # /{a,b}c{a,b}/ matches "aca"
    assert Either((Lit("a"), Lit("b")), Lit("c", Either((Lit("a"), Lit("b"))))).match("aca")

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

def test_not():
    assert not Not(Lit("a")).match("a")
    assert Not(Lit("a")).match("b")
    assert Not(Plus().match(""))
    assert Not(Charset("abc")).match("x")
    assert Not(Range("a", "c")).match("x")
    # assert Lit("abc", Not(Plus())).match("abc")
    # assert Lit("abc", Not(Charset("abc"))).match("abcd")

def test_either_multiple():
    # /{a,b,c}/ matches "a"
    assert Either((Lit("a"), Lit("b"), Lit("c"))).match("a")
    # /{a,b,c}/ doesn't match "ab"
    assert not Either((Lit("a"), Lit("b"), Lit("c"))).match("ab")
    # /{a,b,c}c/ matches "ac"
    assert Either((Lit("a"), Lit("b"), Lit("c")), Lit("c")).match("ac")
    # /{a,b,c}c/ doesn't match "ax"
    assert not Either((Lit("a"), Lit("b"), Lit("c")), Lit("c")).match("ax")
    # /{a,b}c{a,b}/ matches "aca"
    assert Either((Lit("a"), Lit("b"), Lit("c")), Lit("c", Either((Lit("a"), Lit("b"), Lit("c"))))).match("aca")
