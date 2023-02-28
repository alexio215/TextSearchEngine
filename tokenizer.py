import typing


class Tokenizer:
    def tokenize(self, document_text: str) -> typing.List[str]:
        return document_text.lower().split()


class NaiveTokenizer(Tokenizer):
    def tokenize(self, document_text: str) -> typing.List[str]:
        return document_text.replace('.', ' . ').replace(',', ' , ').lower().split()
