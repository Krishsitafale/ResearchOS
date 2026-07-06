"""
Embedding Service

Generates semantic embeddings using
Sentence Transformers.
"""

import numpy as np
from sentence_transformers import SentenceTransformer

from backend.core.config import EMBEDDING_MODEL
from backend.core.logger import logger


class EmbeddingService:

    def __init__(self):

        logger.info(
            f"Loading embedding model: {EMBEDDING_MODEL}"
        )

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        logger.info(
            "Embedding model loaded successfully."
        )

    # --------------------------------------------------------

    def generate_embeddings(
        self,
        texts: list[str]
    ) -> np.ndarray:

        logger.info(
            f"Generating embeddings for {len(texts)} chunks..."
        )

        embeddings = self.model.encode(

            texts,

            normalize_embeddings=True,

            convert_to_numpy=True,

            show_progress_bar=True

        )

        logger.info(
            f"Embedding shape: {embeddings.shape}"
        )

        return embeddings.astype(np.float32)