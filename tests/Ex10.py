import pytest
class TestForYourLastWords:

    def test_last_words(self):
        self.phrase = input("Set a phrase: ")
        assert len(self.phrase) < 15, f"Too much symbols, input less than 15 characters"
