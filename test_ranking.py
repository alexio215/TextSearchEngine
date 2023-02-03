from unittest import TestCase
import ranking


class TestTermCount(TestCase):
    def test_no_matches(self):
        self.assertEqual(0, ranking.term_count(query='t1 t2', document='t3 t4'))

    def test_partial_match(self):
        self.assertEqual(1, ranking.term_count(query='t1 t2', document='t3 t1'))

    def test_repeated_matches(self):
        self.assertEqual(5, ranking.term_count(query='t1 t2', document='t1 t3 t2 t1 t2 t2'))


class TestBooleanTermCount(TestCase):
    def test_no_matches(self):
        self.assertEqual(0, ranking.boolean_term_count(query='t1 t2', document='t3 t4'))

    def test_partial_match(self):
        self.assertEqual(1, ranking.boolean_term_count(query='t1 t2', document='t3 t1'))

    def test_repeated_matches(self):
        self.assertEqual(2, ranking.boolean_term_count(query='t1 t2', document='t1 t3 t2 t1 t2 t2'))