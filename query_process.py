import tokenizer
from documents import DocumentCollection, Document
from index import Index
from typing import List

def process_query(query: str) -> List[str]:
    return tokenizer.tokenize(query)
def format_results(results: List[str], documents: DocumentCollection) -> str:
    '''
    Given the output of search use documents to create a string to be presented to the user.
    :param results: List of doc_ids
    :param documents: DocumentCollection to be used to format results.
    :return: A single string presented to the user.
    '''
    out = ''
    for doc_id in results:
        doc = documents.get(doc_id)
        out += '\n' + format_single_result(doc)
    return out
def format_single_result(doc: Document) -> str:
    return doc.text

def query_process(query: str, documents: DocumentCollection, index: Index) -> str:
    processed_query = process_query(query)
    results = index.search(processed_query)
    formated_results = format_results(results, documents)
    return formated_results