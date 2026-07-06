from groq import Groq

from backend.core.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

from backend.core.prompt import SYSTEM_PROMPT


class LLMService:

    def __init__(self):

        self.client = Groq(

            api_key=GROQ_API_KEY

        )

    # -----------------------------------------------------

    def generate(

        self,

        query: str,

        context: str

    ):

        prompt = f"""

Context:

{context}


Question:

{query}

"""

        response = self.client.chat.completions.create(

            model=GROQ_MODEL,

            temperature=0,

            messages=[

                {

                    "role": "system",

                    "content": SYSTEM_PROMPT

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response.choices[0].message.content