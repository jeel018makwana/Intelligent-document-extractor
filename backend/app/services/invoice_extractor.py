import json
from app.services.base_extractor import BaseExtractor
from app.services.llm_service import LLMService


class InvoiceExtractor(BaseExtractor):

    def __init__(self):
        self.llm = LLMService()

    def extract(self, text: str):

        fields = [
            "invoice_number",
            "vendor_name",
            "invoice_date",
            "total_amount"
        ]

        result = self.llm.extract_fields(text, fields)

        return result