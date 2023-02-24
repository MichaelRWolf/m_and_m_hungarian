"""
Module to test the hungarian_decorator module.
"""

import unittest

import approvaltests

from HungarianDecorator import HungarianDecorator


class TestHungarianDecorator(unittest.TestCase):
    def setUp(self):
        self.decorator = HungarianDecorator()


def test_decorate_from_file():
    pass

    def test_decorate_text(self):
        pass

    def test_decorate_sentence(self):
        sentence = "This is a sentence."
        expected = "This is a sentence."
        actual = self.decorator.decorate_sentence(sentence)
 #       approvaltests.verify(actual, "received.txt")
        approvaltests.verify(actual)

    def test_decorate_token(self, word=""):
        pass

    def test_decorate_word(self):
        pass

    def test_decorate_punctuation(self):
        approvaltests.verify("Stuff")
