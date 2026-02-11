from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")  # léger et rapide
    return _model

def embed_text(text: str):
    model = get_model()
    vec = model.encode([text], normalize_embeddings=True)[0]
    return vec.tolist()