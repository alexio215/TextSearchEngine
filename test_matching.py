from unittest import TestCase

import matching
from matching import *


class Test(TestCase):
    def test_search(self):
        self.assertEquals(['red and yellow'], search('red', ['red and yellow', 'blue and yellow', 'predict color']))
    def test_search_blank(self):
        self.assertEquals([''],search('',['red and yellow', 'blue and yellow', 'predict color']))
    def test_string_match(self):
        self.assertTrue(string_match('red', 'yellow and blue and red'))
    def test_boolean_term_match_blank(self):
        self.assertFalse(matching.boolean_term_match('', 'yellow and blue and red'))
    def test_boolean_term_match(self):
        pass
    def test_string_match_blank(self):
        self.assertFalse(string_match('', 'yellow and blue and red'))
    def test_search_blank_doc(self):
        self.assertEquals([''],search('yellow',[]))
    def test_boolean_term_match_blank_doc(self):
        self.assertFalse(matching.boolean_term_match('yellow', ''))
    def test_string_match_blank_doc(self):
        self.assertFalse(string_match('red', ''))
    def test_string_match_differentiate(self):
        self.assertTrue(string_match('red and b', 'red and blue'))
    def test_boolean_term_match_differntiate(self):
        self.assertTrue(matching.boolean_term_match('red and b', 'red and blue'))
    def test_string_match_only(self):
        self.assertTrue('red and b', 'red and blue')
    def test_string_match_multi_word_query(self):
        self.assertTrue(string_match('red and blue', 'red and blue and yellow and green'))
    def test_boolean_match_multi_word_query(self):
        self.assertTrue(boolean_term_match('red and blue', 'red and blue and yellow and green'))