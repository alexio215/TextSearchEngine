import json
import typing


class Document(typing.NamedTuple):
    doc_id: str
    text: str


class DocumentCollection:
    def __init__(self):
        self.docs: typing.List[Document] = []
    def add_document(self, doc: Document):
        self.docs.append(doc)
    def get_all_docs(self) -> typing.List[Document]:
        return self.docs
    def get(self, doc_id):
        #return self.docs[doc_id]
        for doc in self.docs:
            if doc.doc_id == doc_id:
                return doc
            else:
                return None


class TransformedDocument(typing.NamedTuple):
    doc_id: str
    tokens: typing.List[str]


class TransformedDocumentCollection:
    #Declare the collection
    def __int__(self):
        self.docs: typing.List[TransformedDocument] = []
    def get_all_docs(self) -> typing.List[TransformedDocument]:
        return self.docs
    #Add a document to the collection
    def add_document(self, doc: TransformedDocument):
        self.docs.append(doc)
    #Write the collection to a file
    def write(self, path: str):
        json_data = {'docs': [td._asdict() for td in self.docs]}
        with open(path, 'w') as fp:
            json.dump(obj = json_data, fp= fp)
    @staticmethod
    #Read the collection from a file
    def read(path: str) -> 'TransformedDocumentCollection':
        out = TransformedDocumentCollection()
        with open(path) as fp:
            collection_dict = json.load(fp)
        doc_records = collection_dict['docs']
        for record in doc_records:
            doc = TransformedDocument(doc_id=record['doc_id'], tokens=record['tokens'])
            out.add_document(doc)
        return out
