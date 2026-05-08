from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.ocr_service import OCRService
from app.services.factory import ExtractorFactory
from app.repositories.document_repository import (
    DocumentRepository
)
from app.utils.file_handler import FileHandler

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/extract")
async def extract_document(
    document_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        file_path = await FileHandler.save_file(file)

        ocr_service = OCRService()

        extracted_text = ocr_service.extract_text(
            file_path
        )

        extractor = ExtractorFactory.get_extractor(
            document_type
        )

        if not extractor:

            raise HTTPException(
                status_code=400,
                detail="Invalid document type"
            )

        result = extractor.extract(extracted_text)

        repository = DocumentRepository(db)

        saved_document = repository.save_document(
            document_type,
            result
        )

        return {
            "id": saved_document.id,
            "document_type": saved_document.document_type,
            "data": saved_document.extracted_data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )