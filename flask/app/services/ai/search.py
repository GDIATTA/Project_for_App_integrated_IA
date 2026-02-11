from flask import Blueprint, request, jsonify
import numpy as np
from app.services.db import get_db_connect
from app.services.ai.embedder import embed_text

ai_bp = Blueprint("ai", __name__, url_prefix="/ai")

def cosine(a, b):
    a = np.array(a, dtype=np.float32)
    b = np.array(b, dtype=np.float32)
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.dot(a, b) / denom) if denom != 0 else 0.0

@ai_bp.route("/search")
def semantic_search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"error": "Missing q"}), 400

    query_vec = embed_text(q)
    col = get_db_connect()

    # simple: on charge tous les items (ok si petite base)
    items = list(col.find({"embedding": {"$exists": True}}))

    scored = []
    for it in items:
        score = cosine(query_vec, it["embedding"])
        it["_score"] = score
        it["_id"] = str(it["_id"])
        it.pop("embedding", None)  # on ne renvoie pas le gros vecteur
        scored.append(it)

    scored.sort(key=lambda x: x["_score"], reverse=True)
    return jsonify(scored[:10])