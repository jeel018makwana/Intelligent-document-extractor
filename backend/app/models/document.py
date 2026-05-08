from sqlalchemy import Column, Integer, String, JSON
from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_type = Column(String)
    extracted_data = Column(JSON)