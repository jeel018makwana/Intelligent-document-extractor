from sqlalchemy.orm import Session
from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def save_document(
        self,
        document_type: str,
        extracted_data: dict
    ):

        document = Document(
            document_type=document_type,
            extracted_data=extracted_data
        )

        self.db.add(document)

        self.db.commit()

        self.db.refresh(document)

        return document