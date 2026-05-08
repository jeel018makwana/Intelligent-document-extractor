import json
from app.services.base_extractor import BaseExtractor
from app.services.llm_service import LLMService


class LicenseExtractor(BaseExtractor):

    def __init__(self):
        self.llm = LLMService()

    def extract(self, text: str):

        fields = [
            "name",
            "license_number",
            "dob",
            "valid_upto"
        ]

        result = self.llm.extract_fields(text, fields)

        return result