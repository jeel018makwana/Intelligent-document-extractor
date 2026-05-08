from app.services.aadhaar_extractor import AadhaarExtractor
from app.services.passport_extractor import PassportExtractor
from app.services.license_extractor import LicenseExtractor
from app.services.invoice_extractor import InvoiceExtractor


class ExtractorFactory:

    @staticmethod
    def get_extractor(document_type: str):

        extractors = {
            "aadhaar": AadhaarExtractor(),
            "passport": PassportExtractor(),
            "license": LicenseExtractor(),
            "invoice": InvoiceExtractor()
        }

        return extractors.get(document_type)