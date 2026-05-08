import json

from openai import OpenAI

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def extract_fields(
        self,
        text: str,
        fields: list
    ):

        prompt = f"""
        Extract these fields:

        {fields}

        From this document text:

        {text}

        Return ONLY valid JSON.
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        try:

            return json.loads(content)

        except Exception:

            return {
                "raw_response": content
            }