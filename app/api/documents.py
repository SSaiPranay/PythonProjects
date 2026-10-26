from fastapi import APIRouter,HTTPException,status
from app.models.document import DocumentResponse,DocumentCreate

from app.services.document_service import get_document,create_document,get_documents,delete_document

router = APIRouter(prefix="/documents",tags=["Documents"])


@router.post("/create",
             response_model=DocumentResponse,
             status_code=status.HTTP_201_CREATED
             )
def create_document_api(document:DocumentCreate)->DocumentResponse:
    return create_document(document)


@router.get("/{doument_id}",
            response_model=DocumentResponse)
def get_document_api(document_id:int)->DocumentResponse:
    document= get_document(document_id)
    if not document:
        raise HTTPException(status_code=404,detail="Document Not Found")
    return document

@router.get("/", response_model=list[DocumentResponse])
def get_all_documents() -> list[DocumentResponse]:
    return get_documents()


@router.delete("/{document_id}")
def delete_document_api(document_id:int):
    deleted =delete_document(document_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )
    return {"message":"Document deleted successfully"}

