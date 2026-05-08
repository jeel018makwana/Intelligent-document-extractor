from pydantic import BaseModel
from typing import Dict


class DocumentResponse(BaseModel):
    id: int
    document_type: str
    extracted_data: Dict

    class Config:
        from_attributes = True