import collections
import math
import typing
import json
from collections import defaultdict

import documents
from documents import TransformedDocument, TransformedDocumentCollection


#def count_words(doc: TransformedDocument) -> typing.Dict[str, int]:
#    out = dict()
#    for token in doc.tokens:
#        if token in out:
#            out[token] += 1
#        else:
#            out[token] = 1
#    return out

#def count_words(doc: TransformedDocument) -> typing.Dict[str, int]:
#    out = collections.defaultdict(int)
#    for token in doc.tokens:
#        out[token] += 1
#    return out

def count_words(doc: TransformedDocument) -> collections.Counter:
   return collections.Counter(doc.tokens)

def count_words_in_collection(docs: TransformedDocumentCollection) -> collections.Counter:
    totals = collections.Counter()
    for doc in docs.get_all_docs():
        totals.update(count_words(doc))
    return totals

def document_counts(docs: TransformedDocumentCollection) -> collections.Counter:
    """
    Compute number of documents each word occurs in
    :param docs:
    :return:
    """
    num_docs = collections.Counter()
    for doc in docs.get_all_docs():
        num_docs.update(collections.Counter(set(doc.tokens)))
    return num_docs

def term_frequency(count: int, doc_len: int) -> float:
    return count / doc_len

def inverse_doc_frequency(doc_count: int, collection_size: int) -> float:
     return math.log(collection_size / doc_count)

def tf_idf(tf: float, idf: float) -> float:
    return tf * idf
def doc_tf_idf_scores(doc: TransformedDocument, doc_frequencies: collections.Counter) -> typing.Dict[str, float]:
    out = dict()
    term_frequencies = count_words(doc)
    for term, freq in term_frequencies:
        weight = freq / doc_frequencies[term]
        out[term] = weight
    return out


def tf_idf_scores(docs: TransformedDocumentCollection):
    doc_frequencies = document_counts(docs)
    out = list()
    for doc in docs:
        out.append(doc_tf_idf_scores(doc, doc_frequencies))
    return out

def query_score(query: typing.List[str], doc_weights: typing.Dict[str, float]) -> float:
    return sum([doc_weights[term] for term in query])

def compute_stopwords(docs: TransformedDocumentCollection) -> typing.List[str]:
    #I am aware this is not a pretty solution. I could not figure out how to go into the tuple itself to extract the value
    total_words_in_doc_collection = collections.Counter(count_words_in_collection(docs).most_common(20))
    total_words_in_doc = collections.Counter(document_counts(docs).most_common(20))
    wordsIntersection = list()
    print(set(total_words_in_doc.keys()))
    print(set(total_words_in_doc_collection.keys()))
    for key in set(total_words_in_doc.keys()):
        for second_key in set(total_words_in_doc_collection.keys()):
            if tuple(key)[0] == tuple(second_key)[0]:
                wordsIntersection.append(tuple(key)[0])
    with open('/Users/alexio/Desktop/School/Y2Q2/Soph Lab/stopwords.json', 'w') as fp:
        json.dump(obj=wordsIntersection, fp=fp)
    return wordsIntersection

def get_best_terms(docs: TransformedDocumentCollection, stopWords: list[str]) -> typing.Dict[str, list[str]]:
    docsBestTerms = defaultdict()
    for doc in docs.get_all_docs():
        doc_words = count_words(doc)
        for stopWord in stopWords:
            doc_words.__delitem__(stopWord)
        bestWords = list()
        for key in collections.Counter(doc_words.most_common(10)).keys():
            bestWords.append(tuple(key)[0])
        docsBestTerms[doc.doc_id] = bestWords
        #Work on the one above ^^^
        # unhashable type: 'list'
    with open('/Users/alexio/Desktop/School/Y2Q2/Soph Lab/best_terms.json', 'w') as fp:
        json.dump(obj=docsBestTerms, fp=fp)
    return docsBestTerms