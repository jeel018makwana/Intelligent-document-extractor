import os
from fastapi import UploadFile


class FileHandler:

    @staticmethod
    async def save_file(file: UploadFile):

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            file.filename
        )

        with open(file_path, "wb") as f:

            content = await file.read()

            f.write(content)

        return file_path