from unittest import TestCase

import indexing_process
from indexing_process import *
from documents import *

class FakeTokenizer:
    def tokenize(self, text):
        return text.lower().split()

def create_document_collection():
    docs = DocumentCollection()
    docs.add_document(Document(doc_id='1', text='some text'))
    docs.add_document(Document(doc_id='2', text='some other text'))
    return docs


class TestDocumentTransformer(TestCase):
    def test_run(self):
        document_transformer = DocumentTransformer(FakeTokenizer())
        transformed_docs = document_transformer.transform_documents()
        self.assertEquals([TransformedDocument(doc_id='1', tokens=['some', 'text']),TransformedDocument(doc_id='2', tokens=['some', 'other', 'text'])],transformed_docs.docs)

class FakeSource(indexing_process.Source):
    def read_documents(self):
        docs = DocumentCollection()
        docs.add_document(Document(doc_id = '1', text = 'some text'))
        return docs

class FakeDocumentTransformer(indexing_process.DocumentTransformer):
    def transform_documents(self, document_collection):
        docs = document_collection.get_all_docs()
        output = TransformedDocumentCollection
        for d in docs:
            tokens = tokenize(d.text)
            transformed_doc = TransformedDocument(doc_id=d.doc_id, tokens=tokens)
            output.add_document(transformed_doc)
        return output


class IndexCreator:
    def create_index(self, transformed_documents):
        index = Index()
        for doc in transformed_documents.get_all_docs():
            index.add_document(doc)
        return index

class TestIndexingProcess(TestCase):
    def test_run(self):
        self.fail()
