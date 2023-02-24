"""
Module to test the hungarian_decorator module.
"""

import unittest
import approvaltests
import hungarian_decorator

class TestHungarianDecorator(unittest.TestCase):
    def setUp(self):
        self.decorator = hungarian_decorator.HungarianDecorator()

    def test_decorate_from_file(self):
        pass

    def test_decorate_text(self):
        pass

    def test_decorate_sentence(self):
        sentence = "This is a sentence."
        expected = "This is a sentence."
        actual = self.decorator.decorate_sentence(sentence)
        approvaltests.verify(actual, "received.txt")

    def test_decorate_token(self, word=""):
        fail

    def test_decorate_word(self):
        pass

    def test_decorate_punctuation(self):
        pass
    