from unittest import TestCase

import tokenizer


class Test(TestCase):
    def test_tokenize__separate_words(self):
        self.assertEqual(['some', 'word'], tokenizer.tokenize('some word'))

    def test_tokenize__lower_case(self):
        self.assertEqual(['some', 'word'], tokenizer.tokenize('Some word'))

    def test_tokenize__split_periods(self):
        self.assertEqual(['some', 'word', '.'], tokenizer.tokenize('Some word.'))

    def test_tokenize__split_comma(self):
        self.assertEqual(['some', ',', 'word'], tokenizer.tokenize('Some, word'))
