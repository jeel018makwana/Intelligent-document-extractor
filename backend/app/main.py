from fastapi import FastAPI

from app.api.routes.extraction import router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Intelligent Document Extraction Platform"
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "API Running Successfully"
    }