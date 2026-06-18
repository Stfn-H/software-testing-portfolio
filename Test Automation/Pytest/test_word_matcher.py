import pytest
from word_matcher import count_word_matches

# Exercise 1: Basic Parameterized Tests

@pytest.mark.parametrize("text, target, expected", [
    ("The cat sat on the mat", "cat", 1),
    ("Dog dog DOG dOg", "dog", 4),
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0),
    ("catcat cat catdog", "cat", 1),
    ("a a a", "a", 3)
])
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected


### Exercise 2: Edge Case Testing

# Note: I assumed there is a formatting error in TC6 (a space behind cat - target="cat ")
# so in this case I removed the space

@pytest.mark.parametrize("text, target,expected", [
    ("" ,"word" ,0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello  world", "world", 1),
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1)
])
def test_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected


### Exercise 3: Negative Testing

@pytest.mark.parametrize("text, target", [
    (None, "word"),
    ("hello world", None),
    (123, "word"),
    ("hello world", 456),
    (["hello", "world"], "world"),
    ("hello world", ["world"])
])
def test_type_error_cases(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)
