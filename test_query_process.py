from unittest import TestCase

import tokenizer
from query_process import TokenizerOnlyQueryTransformer, NaiveResultFormatter
from tokenizer import Tokenizer
from documents import *


class FakeTokenizer(Tokenizer):
    def tokenize(self, text):
        return text.lower().split()



class TestTokenizerOnlyQueryTransformer(TestCase):
    def test_tokenize_query(self):
        fakeTokenizer = FakeTokenizer()
        fake_query = 'This is a quick test query'
        fakeTokens = fakeTokenizer.tokenize(fake_query)
        processed_query = TokenizerOnlyQueryTransformer(Tokenizer()).transform_query(fake_query)
        self.assertEqual(fakeTokens, processed_query)


class TestNaiveResultFormatter(TestCase):
    def test_format_results(self):
        fakeDocCollection = DocumentCollection()
        fakeDocCollection.add_document(Document('1', 'This is test doc 1'))
        fakeDocCollection.add_document(Document('2', 'This is test doc 2'))
        fakeResults = ['1', '2']
        formattedResults = NaiveResultFormatter(fakeResults, fakeDocCollection).format_results()
        self.assertEqual(formattedResults, '\nThis is test doc 1\nThis is test doc 2')