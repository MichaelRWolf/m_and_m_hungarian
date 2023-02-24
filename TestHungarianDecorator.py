"""
Module to test the hungarian_decorator module.
"""

import unittest
import approvaltests
from approvaltests.reporters \
    import CommandLineReporter, MultiReporter, GenericDiffReporter
from approvaltests.reporters.generic_diff_reporter_factory \
    import GenericDiffReporterFactory


from HungarianDecorator \
    import HungarianDecorator


class TestHungarianDecorator(unittest.TestCase):
    def setUp(self):
        self.decorator = HungarianDecorator()
        reporter = MultiReporter(GenericDiffReporter.create('sdiff'),
                                 GenericDiffReporter.create('meld'),
                                 CommandLineReporter())

        approvaltests.set_default_reporter(reporter)

    @unittest.skip("Not yet implemented")
    def test_decorate_from_file(self):
        pass

    @unittest.skip("Not yet implemented")
    def test_decorate_text(self):
        pass

    def test_decorate_sentence(self):
        sentence = "This is a sentence."
        actual = self.decorator.decorate_sentence(sentence)
#        approvaltests.verify(actual, reporter=DiffReporter())
# Not yet        r = GenericDiffReporterFactory().get('genericdiff')

        r1 = GenericDiffReporterFactory().get('meld')
        # print(f"{r1}")

        r2 = CommandLineReporter()
        # print(f"{r2}")

        r3 = MultiReporter(r1, r2)

        approvaltests.verify(actual, reporter=r3)

    @unittest.skip("Not yet implemented")
    def test_decorate_token(self, word=""):
        pass

    @unittest.skip("Not yet implemented")
    def test_decorate_word(self):
        pass

    def test_decorate_punctuation(self):
        approvaltests.verify("Stuff")
