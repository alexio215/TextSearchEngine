import typing


def search(query: str, documents: typing.List[str]) -> typing.List[str]:
    #return [doc for doc in documents if boolean_term_match(query, document)]
    out = []
    for doc in documents:
        if boolean_term_match(query=query, document = doc):
            out.append(doc)
    return out

def string_match(query: str, document: str) -> bool:
    return query in document

def boolean_term_match(query: str, document: str) -> bool:
    query_terms: typing.Set[str] = set(query.lower().split())
    document_terms: typing.Set[str] = set(document.lower().split())
    return query_terms.issubset(document_terms)