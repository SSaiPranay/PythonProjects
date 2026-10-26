from uuid import uuid7
from app.models.document import DocumentCreate,DocumentResponse
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "database" / "documents.json"


# documents : dict[str,DocumentResponse]={}
def read_docs():
    with DATA_FILE.open("r",encoding="utf-8") as file:
        return json.load(file)

def write_docs(documents):
    with DATA_FILE.open("w",encoding="utf-8") as file:
        json.dump(documents,file,indent=4)


def create_document(document: DocumentCreate):
    documents = read_docs()

    next_id = max(
        (item["id"] for item in documents),
        default=0,
    ) + 1
    new_document = {
        "id": next_id,
        **document.model_dump(),
    }

    documents.append(new_document)
    write_docs(documents)

    return new_document


def delete_document(document_id: int):
    documents = read_docs()

    updated_documents = [
        document
        for document in documents
        if document["id"] != document_id
    ]

    if len(updated_documents) == len(documents):
        return False

    write_docs(updated_documents)
    return True


def get_documents():
    return read_docs()


def get_document(document_id:str)->DocumentResponse|None:
    # return documents.get(document_id)
    documents=read_docs()
    for document in documents:
        if document["id"]==document_id:
            return document
    return None
