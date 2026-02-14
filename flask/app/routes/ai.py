from flask import Blueprint, jsonify

ai_bp = Blueprint(
    "ai",          # nom interne
    __name__,
    url_prefix="/ai"  # préfixe commun
)

@ai_bp.route("/ping")
def ping():
    return jsonify({"status": "AI alive"})