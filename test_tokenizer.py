from unittest import TestCase

import tokenizer


class Test(TestCase):
    def test_tokenize__seperate_words(self):
        self.assertEquals(['some', 'word'], tokenizer.tokenize('some word'))
    def test_tokenize__lower_case(self):
        self.assertEquals(['some', 'word'], tokenizer.tokenize('Some word'))
    def test_tokenize__split_periods(self):
        self.assertEquals(['some', 'word', '.'], tokenizer.tokenize('Some word.'))
    def test_tokenize__split_comma(self):
        self.assertEquals(['some',',', 'word'], tokenizer.tokenize('Some,word'))