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

# TODO: Store approved files in a separate directory
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

        visual_reporter = GenericDiffReporterFactory().get('meld')
        textual_reporter = CommandLineReporter()
        multi_reporter = MultiReporter(visual_reporter, textual_reporter)

        approvaltests.verify(actual, reporter=multi_reporter)

    @unittest.skip("Not yet implemented")
    def test_decorate_token(self, word=""):
        pass

    @unittest.skip("Not yet implemented")
    def test_decorate_word(self):
        pass

    def test_decorate_punctuation(self):
        approvaltests.verify("Stuff")
