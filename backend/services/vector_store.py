"""
FAISS Vector Store

Responsible for

- Storing embeddings
- Persisting index
- Semantic search
"""

import os
import pickle
from typing import List

import faiss
import numpy as np

from backend.core.logger import logger


class VectorStore:

    def __init__(

        self,

        dimension: int = 384,

        index_path: str = "backend/storage/vector_db/faiss.index",

        metadata_path: str = "backend/storage/vector_db/metadata.pkl"

    ):

        self.dimension = dimension

        self.index_path = index_path

        self.metadata_path = metadata_path

        os.makedirs(

            os.path.dirname(index_path),

            exist_ok=True

        )

        self.index = self._load_index()

        self.documents = self._load_documents()

    # --------------------------------------------------------

    def _load_index(self):

        if os.path.exists(self.index_path):

            logger.info("Loading FAISS index...")

            return faiss.read_index(

                self.index_path

            )

        logger.info("Creating new FAISS index...")

        return faiss.IndexFlatIP(

            self.dimension

        )

    # --------------------------------------------------------

    def _load_documents(self):

        if os.path.exists(

            self.metadata_path

        ):

            with open(

                self.metadata_path,

                "rb"

            ) as file:

                return pickle.load(file)

        return []

    # --------------------------------------------------------

    def add(

        self,

        embeddings: np.ndarray,

        chunks: List[str]

    ):

        self.index.add(

            embeddings.astype(np.float32)

        )

        self.documents.extend(

            chunks

        )

    # --------------------------------------------------------

    def search(

        self,

        query_embedding: np.ndarray,

        top_k: int = 5

    ):

        scores, indices = self.index.search(

            query_embedding.astype(np.float32),

            top_k

        )

        results = []

        for score, idx in zip(

            scores[0],

            indices[0]

        ):

            if idx == -1:

                continue

            results.append(

                {

                    "id": int(idx),

                    "chunk": str(self.documents[idx]),

                    "score": float(score),

                    "retriever": "dense"

                }

            )

        return results

    # --------------------------------------------------------

    def save(self):

        faiss.write_index(

            self.index,

            self.index_path

        )

        with open(

            self.metadata_path,

            "wb"

        ) as file:

            pickle.dump(

                self.documents,

                file

            )

    # --------------------------------------------------------

    def clear(self):

        self.index = faiss.IndexFlatIP(

            self.dimension

        )

        self.documents = []

        self.save()

    # --------------------------------------------------------

    @property
    def size(self):

        return self.index.ntotal