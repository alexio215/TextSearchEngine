from unittest import TestCase
from matching import *


class Test(TestCase):
    def test_search(self):
        self.assertEqual(['red and yellow'],
                         search('red', ['red and yellow', 'blue and yellow', 'predict color']))

    def test_search__empty_query(self):
        self.assertEqual(['red and yellow', 'blue and yellow', 'predict color'],
                         search('', ['red and yellow', 'blue and yellow', 'predict color']))

    def test_search__empty_docs(self):
        self.assertEqual([], search('q', []))


    def test_string_match__matches(self):
        self.assertTrue(string_match('red', 'red and yellow'))

    def test_string_match__dont_match(self):
        self.assertFalse(string_match('red', 'yellow and blue'))

    def test_string_match__match_substring(self):
        self.assertTrue(string_match('red', 'predict color'))

    def test_string_match__empty_query(self):
        self.assertTrue(string_match('', 'predict color'))


    def test_boolean_match__matches(self):
        self.assertTrue(boolean_term_match('red', 'red and yellow'))

    def test_boolean_match__substring(self):
        self.assertFalse(boolean_term_match('red', 'predict color'))

    def test_boolean_match__two_terms_match(self):
        self.assertTrue(boolean_term_match('red blue', 'red and blue'))

    def test_boolean_match__some_match(self):
        self.assertFalse(boolean_term_match('red green', 'red and blue'))
