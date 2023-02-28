from typing import List

from tokenizer import Tokenizer
from documents import DocumentCollection, Document
from index import NaiveIndex, Index
from documents import TransformedDocumentCollection
from indexing_process import IndexingProcess


def process_query(query: str) -> List[str]:
    return Tokenizer.tokenize(query)


class TokenizerOnlyQueryTransformer:
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
    def transform_query(self, query: str):
        return self.tokenizer.tokenize(query)

class NaiveResultFormatter:
    def __init__(self, results: List[str], documents: DocumentCollection):
        self.docs = documents
        self.results = results
    def format_single_result(self, doc: Document) -> str:
        return doc.text

    def format_results(self) -> str:
        """
        Given the output of search use documents to create a string to be presented to the user.
        :param results: List of doc_ids
        :param documents: DocumentCollection to be used to format results.
        :return: A single string presented to the user.
        """
        out = ''
        for doc_id in self.results:
            doc = self.docs.get(doc_id)
            out += '\n' + self.format_single_result(doc)
        return out

class QueryProcess:
    def __init__(self, formatter: NaiveResultFormatter, index: Index, query_transformer: TokenizerOnlyQueryTransformer):
        #self.documents = documents now to be passed into result formatter during declaration
        self.index = index
        self.formatter = formatter
        self.query_transformer = query_transformer
    def run(self, query: str) -> str:
        processed_query = self.query_transformer.transform_query(query)
        results = self.index.search(processed_query)
        formatted_results = self.formatter.format_results(results)
        return formatted_results
    @staticmethod
    def create_naive_indexing_process(index: Index, query_transformer: TokenizerOnlyQueryTransformer):
        QueryProcessesor = QueryProcess(NaiveResultFormatter(), index, query_transformer)
        return QueryProcessesor