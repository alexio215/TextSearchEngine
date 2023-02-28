from unittest import TestCase

import documents
from index import SimpleInvertedIndex
from documents import *

class TestSimpleInvertedIndex(TestCase):
    def test_write(self):
        invertedIndex = SimpleInvertedIndex()
        fakeDoc = documents.TransformedDocument('1',['.', 'test', 'hi'])
        invertedIndex.add_document(fakeDoc)
        invertedIndex.write('/Users/alexio/Desktop/School/Y2Q2/Soph Lab/simple_inverted_index.json')
