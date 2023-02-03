import json
import typing
from documents import Document, DocumentCollection, TransformedDocument, TransformedDocumentCollection
from index import Index
from tokenizer import tokenize


class DictDocumentCollection():
    def __init__(self):
        #Initialize the class where self.docs is a dictionary with default type Document
        self.docs = {}
    def add_document(self, doc: Document):
        #Method to add doc to dictionary. Doc ID as key and Doc as value. (doc_id, doc)
        self.docs[doc.doc_id] = doc
    def get_all_docs(self) -> typing.Dict:
        #Return self.docs distionary as a List of Documents
        return self.docs
    #Write the collection to a file
    def write(self, path: str):
        #What does "td" asdict do
        json_data = self.docs
        with open(path, 'w') as fp:
            json.dump(obj = json_data, fp= fp)
    @staticmethod
    #Read the collection from a file
    def read(path: str) -> 'DictDocumentCollection':
        out = DictDocumentCollection()
        with open(path) as fp:
            #Open where the DictDocCollection was written
            collectionofdictwritten = json.load(fp)
        for docIdInDict in collectionofdictwritten:
            #print(collectionofdictwritten[docIdInDict])
            #print(type(collectionofdictwritten[docIdInDict]))
            docToAddBack = Document(collectionofdictwritten[docIdInDict][0], collectionofdictwritten[docIdInDict][1])
            out.add_document(docToAddBack)
        return out

class LectureTranscriptsSource:
    DEFAULT_PATH = "/Users/alexio/Desktop/School/Y2Q2/Soph Lab/lectures_transcripts2-8.json"
    def read_documents(data_file_path: str = DEFAULT_PATH) -> DictDocumentCollection:
        with open(data_file_path) as fp:
            lecture_transcripts = json.load(fp)
        lecture_collection = DictDocumentCollection()
        for lecture in lecture_transcripts:
            #print(lecture)
            lecture_collection.add_document(Document(doc_id=(lecture['source_name'] + str(lecture['index'])), text=lecture['text']))
        return lecture_collection

class Source:
    def read_documents(self):
        pass

class WikiSource(Source):
    DEFAULT_PATH = "/Users/alexio/Desktop/School/Y2Q2/Soph Lab/wiki_small.json"
    def read_documents(self, data_file_path: str = DEFAULT_PATH) -> DocumentCollection:
        with open(data_file_path) as fp:
            doc_records = json.load(fp)
        doc_collection = DocumentCollection()
        for record in doc_records:
            doc_collection.add_document(Document(doc_id=record['id'], text=record['init_text']))
        return doc_collection

class IndexCreator:
    def create_index(self, transformed_documents):
        index = Index()
        for doc in transformed_documents.get_all_docs():
            index.add_document(doc)
        return index

class DocumentTransformer:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    def transform_documents(self, document_collection):
        docs = document_collection.get_all_docs()
        output = TransformedDocumentCollection
        for d in docs:
            tokens = self.tokenizer.tokenize(d.text)
            transformed_doc = TransformedDocument(doc_id=d.doc_id, tokens=tokens)
            output.add_document(transformed_doc)
        return output


class IndexingProcess:
    def __init__(self, tokenizer, document_transformer, index_creator):
        self.tokenizer = tokenizer
        self.document_transformer = document_transformer
        self.index_creator = index_creator
    def run(document_source: Source) -> (DocumentCollection, Index):
        #Retrieve collection of docs
        document_collection = document_source.read_documents()
        #transform the docs
        transformed_documents = self.document_transformer.transform_documents(document_collection)
        #transformed_documents.write('')
        #create the index for the docs and their contents
        index = self.index_creator.create_index(transformed_documents)
        return (document_collection, index)
