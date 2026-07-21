import pytest
class TestForYourLastWords:

    def test_last_words(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Too much symbols, input less than 15 characters"
