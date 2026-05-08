from dependency_injector import containers, providers

from app.services.ocr_service import OCRService


class Container(containers.DeclarativeContainer):

    ocr_service = providers.Singleton(
        OCRService
    )