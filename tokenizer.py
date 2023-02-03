import typing
def tokenize(document_text) -> typing.List:
    return document_text.replace('.',' . ').replace(',', ' , ').lower().split()
