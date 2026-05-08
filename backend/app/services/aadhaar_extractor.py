import json
from app.services.base_extractor import BaseExtractor
from app.services.llm_service import LLMService


class AadhaarExtractor(BaseExtractor):

    def __init__(self):
        self.llm = LLMService()

    def extract(self, text: str):

        fields = [
            "name",
            "aadhaar_number",
            "dob",
            "gender"
        ]

        result = self.llm.extract_fields(text, fields)

        return result