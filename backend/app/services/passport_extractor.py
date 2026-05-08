import json
from app.services.base_extractor import BaseExtractor
from app.services.llm_service import LLMService


class PassportExtractor(BaseExtractor):

    def __init__(self):
        self.llm = LLMService()

    def extract(self, text: str):

        fields = [
            "name",
            "passport_number",
            "nationality",
            "date_of_birth",
            "expiry_date"
        ]

        result = self.llm.extract_fields(text, fields)

        return result