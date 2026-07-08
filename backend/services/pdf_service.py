"""
PDF Processing Service

Responsible for:

- Opening PDF
- Reading pages
- Extracting text
"""

from annotated_types import doc
import fitz

from backend.core.logger import logger


class PDFService:

    def extract_text(
        self,
        pdf_path: str
    ) -> str:

        logger.info(
            f"Opening PDF: {pdf_path}"
        )

        document = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(document):

            logger.info(
                f"Reading page {page_number + 1}"
            )

            pages.append(

                page.get_text()

            )

        document.close()

        text = "\n".join(pages)

        logger.info(

            f"Extracted {len(text)} characters."

        )

        return text
    
    def page_count(self, pdf_path: str):

        import fitz

        doc = fitz.open(pdf_path)

        pages = len(doc)

        doc.close()

        return pages