from task1 import check_word
import pytest

def test_word(good_word, bad_word):
    assert good_word, check_word(bad_word)

if __name__ == "__main__":
    pytest.main(['-vv'])
