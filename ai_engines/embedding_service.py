from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates sentence embeddings using a SentenceTransformer model.
    """

    def __init__(self,
                 model_name: str = "all-MiniLM-L6-v2"):

        self.model = SentenceTransformer(model_name)

    def encode(self, texts):

        return self.model.encode(
            texts,
            convert_to_numpy=True
        )

# service = EmbeddingService()

# embeddings = service.encode([
#     "Autonomous rover navigation",
#     "Semantic search using transformers"
# ])

# print(embeddings.shape)