from documents import *
from unittest import TestCase


def create_test_dict_doc_collection() -> DictDocumentCollection:
    docs = DictDocumentCollection()
    docs.add_document(Document(doc_id='1', text='text1'))
    docs.add_document(Document(doc_id='2', text='text2'))
    return docs


class TestDictDocumentCollection(TestCase):
    def test_add_document(self):
        collection = create_test_dict_doc_collection()
        self.assertEqual(
            {'1': Document(doc_id='1', text='text1'), '2': Document(doc_id='2', text='text2')},
            collection.docs
        )

    def test_get_all_docs(self):
        collection = create_test_dict_doc_collection()
        self.assertEqual(
            {Document(doc_id='1', text='text1'), Document(doc_id='2', text='text2')},
            set(collection.get_all_docs())
        )

    def test_get(self):
        collection = create_test_dict_doc_collection()
        self.assertEqual(Document(doc_id='1', text='text1'), collection.get(doc_id='1'))
        self.assertEqual(Document(doc_id='2', text='text2'), collection.get(doc_id='2'))
        self.assertIsNone(collection.get(doc_id='3'))
