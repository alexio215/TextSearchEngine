from unittest import TestCase
import indexing_process
from indexing_process import *
from documents import *


class FakeTokenizer(Tokenizer):
    def tokenize(self, text):
        return text.lower().split()


def create_document_collection():
    docs = DocumentCollection()
    docs.add_document(Document(doc_id='1', text='some text'))
    docs.add_document(Document(doc_id='2', text='some other text'))
    return docs


class TestTokenizerOnlyDocumentTransformer(TestCase):
    def test_run(self):
        document_transformer = TokenizerOnlyDocumentTransformer(FakeTokenizer())
        transformed_docs = document_transformer.transform_documents(create_document_collection())
        self.assertEqual([TransformedDocument(doc_id='1', tokens=['some', 'text']),
                          TransformedDocument(doc_id='2', tokens=['some', 'other', 'text'])],
                         transformed_docs.docs)


class FakeSource(indexing_process.Source):
    def read_documents(self):
        docs = DocumentCollection()
        docs.add_document(Document(doc_id='1', text='some text'))
        return docs


class FakeDocumentTransformer(indexing_process.DocumentTransformer):
    def transform_documents(
            self, document_collection: DocumentCollection) -> TransformedDocumentCollection:
        docs = document_collection.get_all_docs()
        out = TransformedDocumentCollection()
        for d in docs:
            transformed_doc = TransformedDocument(doc_id=d.doc_id, tokens=[d.text])
            out.add_document(transformed_doc)
        return out


class FakeIndex(Index):
    def __init__(self):
        self.docs = []

    def add_document(self, doc: TransformedDocument):
        self.docs.append(doc)


class TestIndexingProcess(TestCase):
    def test_run(self):
        process = indexing_process.IndexingProcess(
            document_transformer=FakeDocumentTransformer(),
            index=FakeIndex()
        )
        doc_collection, index = process.run(FakeSource())
        self.assertEqual([Document(doc_id='1', text='some text')], doc_collection.docs)
        self.assertEqual([TransformedDocument(doc_id='1', tokens=['some text'])], index.docs)
