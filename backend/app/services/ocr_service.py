import pytesseract
from PIL import Image
from app.core.logger import logger
from app.core.exceptions import OCRException

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRService:

    def extract_text(self, image_path: str) -> str:

        try:
            image = Image.open(image_path)

            text = pytesseract.image_to_string(image)

            logger.info("OCR extraction successful")

            return text

        except Exception as e:
            logger.error(str(e))
            raise OCRException("OCR failed")