from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from backend.core.dependencies import (
    embedding_service,
    vector_store,
    bm25_service,
)

from backend.core.logger import logger

from backend.services.chunk_service import ChunkService
from backend.services.pdf_service import PDFService

router = APIRouter()

# --------------------------------------------------------

UPLOAD_DIRECTORY = Path("backend/storage/uploads")

UPLOAD_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------------

pdf_service = PDFService()

chunk_service = ChunkService()

# --------------------------------------------------------


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    logger.info("=" * 60)
    logger.info("Document Upload Started")
    logger.info("=" * 60)

    # ----------------------------------------------------
    # Validate file
    # ----------------------------------------------------

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # ----------------------------------------------------
    # Save PDF
    # ----------------------------------------------------

    destination = UPLOAD_DIRECTORY / file.filename

    with open(destination, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    logger.info(
        f"Saved PDF : {destination}"
    )

    # ----------------------------------------------------
    # Extract Text
    # ----------------------------------------------------

    extracted_text = pdf_service.extract_text(
        str(destination)
    )

    if not extracted_text.strip():

        raise HTTPException(
            status_code=400,
            detail="No text could be extracted from the PDF."
        )

    logger.info(
        f"Characters Extracted : {len(extracted_text)}"
    )

    # ----------------------------------------------------
    # Chunk Text
    # ----------------------------------------------------

    chunks = chunk_service.chunk_text(
        extracted_text
    )

    logger.info(
        f"Generated {len(chunks)} chunks."
    )

    # ----------------------------------------------------
    # Generate Embeddings
    # ----------------------------------------------------

    embeddings = embedding_service.generate_embeddings(
        chunks
    )

    logger.info(
        f"Embeddings Shape : {embeddings.shape}"
    )

    # ----------------------------------------------------
    # Store in FAISS
    # ----------------------------------------------------

    vector_store.add(
        embeddings,
        chunks
    )

    vector_store.save()
    
    bm25_service.build_index()

    logger.info(
        f"Total vectors stored : {vector_store.size}"
    )

    logger.info("=" * 60)
    logger.info("Document Upload Complete")
    logger.info("=" * 60)

    # ----------------------------------------------------

    return {

        "status": "success",

        "filename": file.filename,

        "characters": len(extracted_text),

        "num_chunks": len(chunks),

        "embedding_dimension": embeddings.shape[1],

        "total_vectors": vector_store.size

    }