import typing

from documents import TransformedDocument


class Index:
    def __int__(self):
        self.docs = dict()
    def add_document(self, doc: TransformedDocument):
        self.docs[doc.doc_id] = set(doc.tokens)
    def search(self, query: typing.List[str]) -> typing.List[str]:
        '''
        Does search using the index.
        :param query: List of query terms
        :return: List of doc_ids for matching documents in the correct order.
        '''
        query_terms_set = set(query)
        matching_doc_ids = []
        for doc_id, doc_terms in self.docs.items():
            if query_terms_set.issubset(doc_terms):
                matching_doc_ids.append(doc_id)
        return matching_doc_ids
